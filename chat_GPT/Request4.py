import tkinter as tk
from openai import OpenAI
import os

# Fonction pour envoyer la question à l'API GPT et afficher la réponse
def send_to_gpt():
    user_input = user_input_box.get("1.0", "end-1c")  # Récupère l'entrée de l'utilisateur
    # Assurez-vous d'avoir accès à GPT-4 avec votre clé API
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}], 
        model="gpt-4-0613"  # Changez ici pour le modèle GPT-4
    )
    response_box.config(state=tk.NORMAL)
    response_box.delete("1.0", tk.END)
    response_box.insert(tk.END, response.choices[0].message.content)  # Affiche la réponse
    response_box.config(state=tk.DISABLED)
    # ... (le reste de la fonction reste inchangé)

# Configuration du client OpenAI
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Configuration de la fenêtre Tkinter avec un thème sombre
window = tk.Tk()
window.title("Chat GPT")

# Couleurs pour le thème sombre
dark_background = "#36393f"
dark_text = "#ffffff"

# Configuration de la zone de texte pour l'entrée de l'utilisateur avec un thème sombre
user_input_box = tk.Text(window, height=5, width=50, bg=dark_background, fg=dark_text)
user_input_box.pack()

# Bouton pour envoyer la demande avec un thème sombre
send_button = tk.Button(window, text="Envoyer", command=send_to_gpt, bg="#40444b", fg=dark_text)
send_button.pack()

# Configuration de la zone de texte pour afficher la réponse avec un thème sombre
response_box = tk.Text(window, height=10, width=50, bg=dark_background, fg=dark_text, state=tk.DISABLED)
response_box.pack()

# Changer la couleur de fond de la fenêtre
window.configure(bg=dark_background)

window.mainloop()
