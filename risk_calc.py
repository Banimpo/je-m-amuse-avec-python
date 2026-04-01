position = input('Desirez vous acheter ou vendre: ').lower()

if position == "acheter":
    dir = 1
elif position == "vendre" : 
    dir = 0


capital = float(input('Veuillez entrer votre capital: '))

risk_pct = float(input('Entrez le pourcentage que vous voulez : '))

price_enter = float(input("Quel est le prix d'entrée de la transaction: "))

stop_loss = float(input("Quel est le prix de votre stop loss: "))

#CALCUL DE LA SOMME A RISQUER
risk = capital*risk_pct/100

#CALCUL DE LA DISTANCE ENTRE LE P_E ET LE SL
if dir == 1 :
   distance = price_enter - stop_loss
elif dir == 0 :
   distance =stop_loss - price_enter  

#CALCUL DU RISQUE EN LOT A PRENDRE
lot = risk / distance

#Sortie de la somme a investir
print(f'La somme que vous devez investir est de : {risk} ')

#Sortie de la taille de position a prendre
print(f'la taille de votre position est de {lot}')