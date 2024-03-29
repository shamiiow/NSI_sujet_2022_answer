def renverse(mot):
    return "".join(mot[::-1])

assert renverse("informatique") == "euqitamrofni"


def crible(N):
   
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, N, i):
                tab[multiple] = False

    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
