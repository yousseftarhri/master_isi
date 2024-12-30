"""1) Ecrire une fonction retourne(n) qui inverse et renvoie 1'ordre des chiffres d'un nombre
entier n. Par exemple: retourne(47)=74, retourne(20)=2."""
def retourne(n):
    nb_inverse = 0
    while n != 0:
        nb_inverse = nb_inverse*10+n%10
        n = n//10
    return nb_inverse
print(retourne(1221))

"""2) Ecrire une fonction palindrome() qui renyoie true si le nombre est palindrome , 
et false sinon."""
def est_palindrome(n):
    if retourne(n)==n:
        return True
    return False
print(est_palindrome(1221))

"""3)Sachant que 16677 est le premier nombre nécessitant plus de 50 itérations pour produire un
palindrome. Ecrivez une fonction nombreLychrel(n) qui renvoie true, si le nombre entier n
inférieur ou égal 10800, est un nombre de Lychrel et false sinon.
"""
def nombreLychrel(n):
    if n > 10800:
        print("Le nombre doit être inférieur ou égal à 10800.")

    iterations = 0
    while iterations < 50:
        n += int(str(n)[::-1])  # Ajouter le nombre à son inverse
        if est_palindrome(n):
            return False  # Ce n'est pas un nombre de Lychrel
        iterations += 1

    return True  # Si aucune itération ne produit un palindrome, c'est un nombre de Lychrel


# Exemple d'utilisation
print(nombreLychrel(196))  # True
print(nombreLychrel(349))  # False