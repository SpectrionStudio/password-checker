# Password Checker

Un petit vérificateur de mot de passe en Python. Il vérifie quatre règles, donne un niveau de solidité et indique quelles règles ne sont pas respectées.

## Utilisation

Lancez le programme dans un terminal :

```
python password_checker.py
```

Saisissez ensuite le mot de passe à tester.

Exemple avec `bonjour` :

```
Quel est votre mot de passe ? bonjour
Mot de passe fragile
Il manque une majuscule.
Il manque un chiffre.
Il manque un caractère spécial.
Le mot de passe est inférieur à 10 caractères.
```

## Règles vérifiées

- Longueur : au moins 10 caractères
- Au moins une majuscule
- Au moins un chiffre
- Au moins un caractère spécial

## Niveaux

Chaque règle respectée ajoute 1 point au score :

- 4 points : mot de passe solide
- 2 ou 3 points : mot de passe suffisant
- 0 ou 1 point : mot de passe fragile

## Ce que j'ai appris

J'ai voulu réapprendre les bases de Python pour reprendre le code en main : les conditions, les boucles, les variables booléennes. C'était un petit exercice pour me remettre sur le chemin tranquillement, en utilisant le terminal et en initialisant un dépôt avec Git et GitHub.
