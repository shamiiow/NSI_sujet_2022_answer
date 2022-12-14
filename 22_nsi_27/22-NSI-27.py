def taille(a, L):
    if a[L] == ['', '']:
        return 1
    if a[L][0] == '':
        return 1 + taille(a, a[L][1])
    if a[L][1] == '':
        return 1 + taille(a, a[L][1])
    return 1 + taille(a, a[L][1]) + taille(a, a[L][0])

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

assert taille(a, 'F') == 9

def tri_iteratif(tab):
    for k in range( len(tab) , 0, -1):
        imax = k-1
        for i in range(0, k-1):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k-1]:
            tab[k-1], tab[imax] = tab[imax], tab[k-1]
    return tab

assert tri_iteratif([41, 55, 21, 18, 12, 6, 25]) == [6, 12, 18, 21, 25, 41, 55]
