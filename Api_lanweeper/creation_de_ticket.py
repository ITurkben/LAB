import requests

# Remplacez par vos informations
server_url = "http://support.groupe-lepine.com:81"
api_key = "8b8f52b8-153e-49a0-9dba-77c283ddf2a2"
subject = "Example"
description = "Example"
ticket_type = "Demande de service"
priority = "Normal"
username = "groupe-lepine\\abo"  # Remplacez par le nom d'utilisateur approprié
agent_username = "groupe-lepine\\abo"  # Remplacez par le nom d'utilisateur de l'agent
team = "Support Technique"
custom_fields = '{"customFields":[{"name":"error","value":"confirmed bug"}]}'

# Construction de l'URL de la requête
url = f"{server_url}/api.aspx?Action=AddTicket&Key={api_key}&Subject={subject}&Description={description}&Type={ticket_type}&Priority={priority}&Username={username}&AgentUsername={agent_username}&Team={team}"

# Envoi de la requête GET
response = requests.get(url)

# Affichage des résultats
print(f"Statut de la réponse : {response.status_code}")
print(f"Corps de la réponse : {response.text}")
