# Exemple de structure pour enregistrer une ligne
nom_actif = input("Quel actif as-tu來自 tradé ? ")
resultat = input("Gagné (G) ou Perdu (P) ? ")
profit = float(input("Quel est la somme que vous avez gagné ou perdu : "))
commentaires = input("Voulez vous ajouter un commentaire?: ")


# On ouvre le fichier en mode "a" (pour Append / Ajouter)
with open("mon_journal.txt", "a") as fichier:
    # \n sert à passer à la ligne suivante pour le prochain trade
    fichier.write(f" vous avez pris un trade sur le: {nom_actif}\n Vous avez obtenu un trade: {resultat}\n Vous avez enregistré un profit de:{profit}\n Voici votre commentaire :{commentaires}")

print("Trade enregistré avec succès !")