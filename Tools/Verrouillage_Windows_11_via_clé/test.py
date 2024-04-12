import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
# La clé pourrait être stockée de manière plus sécurisée ou récupérée depuis un emplacement distant
AUTH_KEY = "123456"

def ask_for_key():
    while True:
        userInput = simpledialog.askstring(title="Verrouillage de Sécurité",
                                           prompt="Entrez votre clé d'authentification :")
        if userInput == AUTH_KEY:
            break
        else:
            tk.messagebox.showerror("Erreur", "Clé d'authentification incorrecte")

ask_for_key()
