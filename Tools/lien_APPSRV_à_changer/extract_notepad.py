import subprocess
import os
import pandas as pd
import re
import ipaddress

def est_ip_valide(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def extraire_ips_fichier(fichier_log, domaine_cible):
    ips = set()
    if not os.path.exists(fichier_log):
        print(f"Le fichier {fichier_log} n'existe pas.")
        return ips

    with open(fichier_log, 'r', errors='ignore') as fichier:
        print(f"Ouverture du fichier : {fichier_log}")
        for ligne in fichier:
            if domaine_cible in ligne:
                try:
                    ip = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', ligne).group()
                    if est_ip_valide(ip):
                        ips.add(ip)
                except AttributeError:
                    pass
    return ips

def nslookup_sur_ips(adresses_ip):
    resultats_nslookup = {}
    for ip in adresses_ip:
        print(f"nslookup sur : {ip}")
        try:
            process = subprocess.run(['nslookup', ip], capture_output=True, text=True, check=True)
            output = process.stdout
            nom = re.search(r'Name:\s*(\S+)', output)
            if nom:
                resultats_nslookup[ip] = nom.group(1)
            else:
                resultats_nslookup[ip] = "Nom introuvable"
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de nslookup pour l'adresse {ip}: {e}")
            resultats_nslookup[ip] = "Erreur lors de la recherche"
    return resultats_nslookup

def sauvegarder_en_excel(resultats, fichier_sortie):
    # Transformer les résultats en DataFrame
    df = pd.DataFrame(list(resultats.items()), columns=['Adresse IP', 'Nom de Domaine'])
    print(f"Nombre d'entrées à sauvegarder : {len(df)}")  # Vérifier le nombre d'entrées
    
    if not df.empty:  # Vérifier si le DataFrame n'est pas vide
        # Sauvegarder le DataFrame dans un fichier Excel
        df.to_excel(fichier_sortie, index=False)
        print(f"Les résultats ont été sauvegardés dans {fichier_sortie}")
    else:
        print("Aucune donnée à sauvegarder.")


# Chemin vers le fichier de log et le domaine cible
fichier_log = r"C:\Users\itu\Documents\LAB\Tools\lien_APPSRV_à_changer\dnsdebug.txt"
domaine_cible = "(6)appsrv(13)groupe-lepine(3)com(0)"
fichier_sortie = r"C:\Users\itu\Documents\LAB\Tools\lien_APPSRV_à_changer\resultats_dns.xlsx"  # Définir le chemin du fichier Excel de sortie

print("Extraction des adresses IP...")
ips_requetes_dns = extraire_ips_fichier(fichier_log, domaine_cible)

if ips_requetes_dns:
    print("Exécution de nslookup sur les adresses IP extraites...")
    resultats_nslookup = nslookup_sur_ips(ips_requetes_dns)
    sauvegarder_en_excel(resultats_nslookup, fichier_sortie)
else:
    print("Aucune adresse IP correspondante trouvée.")
