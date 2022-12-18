def RechercheMin(tab):
    i_Min = 0
    for i in range(len(tab)):
        if tab[i] < tab[i_Min]:
            i_Min = i
    return i_Min

assert RechercheMin([5]) == 0
assert RechercheMin([2, 4, 1]) == 2
assert RechercheMin([5, 3, 2, 2, 4]) == 2

def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j:
        if tab[i] == 0 :
            i = i+1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j-1
    return tab

assert separe([1,0,1,0,1,0,1,0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

