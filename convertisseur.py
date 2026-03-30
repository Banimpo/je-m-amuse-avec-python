#Declaration de variables
taux = 1.10

#Demande la somme en dollar a l'user
dollar = float(input("VEUILLEZ ENTRER LA SOMME S'IL VOUS PLAIT: "))


#Converssion de la sommme en euros
euro = dollar*taux

#Affichage de la somme en euros
print(f'Vos {dollar} dollars sont égales a {euro} euros')

