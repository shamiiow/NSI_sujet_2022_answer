from random import randint
def tri_selection(tab):
    for k in range(len(tab)):
        i_min = k
        for i in range(k, len(tab)):
            if tab[i_min] > tab[i]:
                i_min = i
        tab[k], tab[i_min] = tab[i_min], tab[k]
    return tab

assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52]


def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ",nb_mystere)
        print("Nombre d'essais: ",compteur)
    else:
        print ("Perdu ! Le nombre etait ",nb_mystere)
plus_ou_moins()