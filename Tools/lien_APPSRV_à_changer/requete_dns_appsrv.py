""" Ce script permet de lister toutes les machines qui font des requetes DNS via le fichier de log des requetes DNS"""

import subprocess
import os

def extraire_ips_fichier(fichier_log, domaine_cible):
    ips = set()
    if not os.path.exists(fichier_log):  # Vérifier si le fichier existe
        print(f"Le fichier {fichier_log} n'existe pas.")
        return ips

    with open(fichier_log, 'r', errors='ignore') as fichier:
        print(f"Ouverture du fichier : {fichier_log}")
        for ligne in fichier:
            if domaine_cible in ligne:
                try:
                    partie_udp = ligne.split("UDP")[1].strip()
                    ip = partie_udp.split()[1]
                    ips.add(ip)
                except IndexError:
                    pass
    return ips

def nslookup_sur_ips(adresses_ip):
    resultats_nslookup = {}
    for ip in adresses_ip:
        print(f"nslookup sur : {ip}")
        try:
            process = subprocess.run(['nslookup', ip], capture_output=True, text=True, check=True)
            output = process.stdout
            print(output)  # Ajout pour voir la sortie brute
            
            lines = output.split('\n')
            for line in lines:
                if 'Name:' in line:
                    nom = line.split(':')[1].strip()
                    resultats_nslookup[ip] = nom
                    break
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de nslookup pour l'adresse {ip}: {e}")
    return resultats_nslookup


# Chemin vers le fichier de log et le domaine cible
fichier_log = r"C:\Users\itu\Documents\LAB\Tools\lien APPSRV à changer\dnsdebug.txt"
domaine_cible = "(6)appsrv(13)groupe-lepine(3)com(0)"

print("Extraction des adresses IP...")
ips_requetes_dns = extraire_ips_fichier(fichier_log, domaine_cible)

if ips_requetes_dns:  # Continuer seulement si des IPs ont été trouvées
    print("Exécution de nslookup sur les adresses IP extraites...")
    resultats_nslookup = nslookup_sur_ips(ips_requetes_dns)

    # Après avoir exécuté nslookup sur toutes les adresses IP
    print("Résultats :")
    for ip, nom in resultats_nslookup.items():
        if nom:  # S'assurer que le nom a été trouvé
            print(f"{ip}: {nom}")
        else:
            print(f"{ip}: Nom introuvable")
else:
    print("Aucune adresse IP correspondante trouvée.")
