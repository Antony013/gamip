# - Faire un jeu en python en mode :
# select 1 pour générer une adresse de nimporte quelle classe et saisir en 2 cout max la classe associé a l'ip
# select 2 pour saisir une adresse qui appartient a une classe random en 2 cout max

# classe a : de 0.0.0.0 à 127.255.255.255
# classe b : de 128.0.0.0 à 191.255.255.255
# classe c : de 192.0.0.0 à 223.255.255.255
# classe d : de 224.0.0.0 à 239.255.255.255
# classe e : de 240.0.0.0 à 255.255.255.255
import random
from random import randint
import getpass

classeA = [("0.0.0.0"), ("127.255.255.255")]
classeB = [("128.0.0.0"), ("191.255.255.255")]
classeC = [("192.0.0.0"), ("223.255.255.255")]
classeD = [("224.0.0.0"), ("239.255.255.255")]
classeE = [("240.0.0.0"), ("255.255.255.255")]


def check_ip_in_class(ip, ip_start, ip_end):
    if ip >= ip_start and ip <= ip_end:
        return True
    return False


def generate_random_ip():
    return '.'.join(str(randint(0, 255)) for _ in range(4))


# nbGame = random.randint(1, 2)

nbGame = int(getpass.getpass(
    "\n1 - Donner une adresse ip v4 d'une classe donné aléatoirement\n2 - Retrouver la classe associé à l'adresse ip v4 généré aléatoirement\n"))

if nbGame == 1:
    nbInput = 0

    random_class = random.choice(
        ["classe A", "classe B", "classe C", "classe D", "classe E"])

    if random_class == "classe A":
        class_ip = classeA
    elif random_class == "classe B":
        class_ip = classeB
    elif random_class == "classe C":
        class_ip = classeC
    elif random_class == "classe D":
        class_ip = classeD
    elif random_class == "classe E":
        class_ip = classeE

    while nbInput < 3:
        ip = input("Donner une adresse de la " + random_class + " : ")

        if check_ip_in_class(ip, class_ip[0], class_ip[1]):
            print("gg")
            break

        nbInput = nbInput + 1

        if nbInput == 3:
            print(
                "Vous avez atteint le nombre total d'essai, revoyez les différentes classe IP v4.")
        else:
            print("ré essaie")

elif nbGame == 2:
    random_ip = generate_random_ip()
    nbInput = 0

    while nbInput < 3:
        input_class = input(
            "Donner la classe de l'adresse ip v4 " + random_ip + " : ")

        if input_class == "classe A":
            class_ip = classeA
        elif input_class == "classe B":
            class_ip = classeB
        elif input_class == "classe C":
            class_ip = classeC
        elif input_class == "classe D":
            class_ip = classeD
        elif input_class == "classe E":
            class_ip = classeE
        else:
            print("La classe saisie n'est pas répertorié.")

        if check_ip_in_class(random_ip, class_ip[0], class_ip[1]):
            print("gg")
            break

        nbInput = nbInput + 1

        if nbInput == 3:
            print(
                "Vous avez atteint le nombre total d'essai, revoyez les différentes classe IP v4.")
        else:
            print("ré essaie")
else:
    print("Erreur dans le choix du jeu.")
