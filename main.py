import random

def jeu():

    #print("Choissisez la borne minimale et la borne maximale pour le jeu.")
    nombre = random.randint(1,1000)
    nb_essais = 0
    essai = -1

    print("J’ai choisi un nombre au hasard entre borne_minimale et borne_maximale. À vous de le deviner...")
    #print(nombre)
    while essai != nombre:
        essai = int(input("Entrer votre essai: "))
        nb_essais = nb_essais + 1

        if essai > nombre:
            print("Mauvais choix, le nombre est plus petit que {}.".format(essai))
        elif essai < nombre:
            print("Mauvaise réponse, le nombre est plus grand que {}.".format(essai))

    if essai == nombre:
        print("Bravo! Bonne réponse! Vous l'avez eu en {} essais.".format(nb_essais))

jeu()

rejouer = input("Voulez-vous faire une autre partie (o/n)?")
if rejouer == "o":
    jeu()
elif rejouer == "n":
    print("Merci et au revoir…")