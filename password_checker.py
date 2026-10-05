import string

password = input("Quel est votre mot de passe ? ")
a_maj = False
a_chiffre = False
a_special = False
longueur_ok = len(password) >= 10

for letter in password:
    if letter in string.ascii_uppercase:
        a_maj = True

    if letter in string.digits:
        a_chiffre = True

    if letter in string.punctuation:
        a_special = True

score = 0
if a_maj == True:
    score = score + 1
if a_chiffre == True:
    score = score + 1
if a_special == True:
    score = score + 1
if longueur_ok == True:
    score = score + 1

if score == 4:
    print("Mot de passe solide")
elif score >= 2:
    print("Mot de passe suffisant")
else:
    print("Mot de passe fragile")
    if a_maj == False:
        print("Il manque une majuscule.")
    if a_chiffre == False:
        print("Il manque un chiffre.")
    if a_special == False:
        print("Il manque un caractère spécial.")
    if longueur_ok == False:
        print("Le mot de passe est inférieur à 10 caractères.")


