def recherche(tab, n):
    indice_d = 0
    indice_f = len(tab)
    while True:
        indice_m = ((indice_f + indice_d) // 2)
        if indice_d > indice_f:
            return -1
        if tab[indice_m] == n:
            return indice_m
        if tab[indice_m] > n:
            indice_f = ((indice_f + indice_d) // 2) - 1
        if tab[indice_m] < n:
            indice_d = ((indice_f + indice_d) // 2) + 1


assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    return ALPHABET.find(lettre)


def cesar(message, decalage):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultat = ''
    for lettre in message:
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre)+decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
