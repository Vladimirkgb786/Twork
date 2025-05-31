import tkinter as tk

# Fonction pour convertir une lettre en langage TWORK
def lettre_twork(lettre):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lettre = lettre.lower()
    if lettre in alphabet:
        position = alphabet.index(lettre)
        nouvelle_position = (position + 7) % 26
        nouvelle_lettre = alphabet[nouvelle_position]
        valeur_division = round((nouvelle_position + 1) / 3, 2)
        return f"{nouvelle_lettre}{valeur_division}"
    elif lettre == " ":
        return "0.5"
    else:
        return lettre  # Garder les caractères spéciaux tels quels

# Fonction pour coder un texte en langage TWORK
def coder_twork():
    texte_original = entree_texte.get("1.0", tk.END).strip()
    texte_twork = " ".join(lettre_twork(lettre) for lettre in texte_original)
    sortie_texte.delete("1.0", tk.END)
    sortie_texte.insert(tk.END, texte_twork)

# Création de l'interface utilisateur
fenetre = tk.Tk()
fenetre.title("TWORK CODER")

# Zone pour entrer le texte original
label_original = tk.Label(fenetre, text="Entrez le texte à coder :")
label_original.pack()
entree_texte = tk.Text(fenetre, height=10, width=50)
entree_texte.pack()

# Bouton pour convertir le texte
bouton_convertir = tk.Button(fenetre, text="Convertir en TWORK", command=coder_twork)
bouton_convertir.pack()

# Zone pour afficher le texte converti
label_sortie = tk.Label(fenetre, text="Texte en langage TWORK :")
label_sortie.pack()
sortie_texte = tk.Text(fenetre, height=10, width=50)
sortie_texte.pack()

# Lancement de l'interface
fenetre.mainloop()