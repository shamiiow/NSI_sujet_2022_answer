def recherche(n, list):
    nb_o = 0
    for i in range(len(list)):
        if list[i] == n:
            nb_o += 1
    return nb_o

assert recherche(5,[]) == 0
assert recherche(5,[-2,3,4,8]) == 0
assert recherche(5,[-2,3,1,5,3,7,4]) == 1
assert recherche(5,[-2,5,3,5,4,5]) == 3

def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu

assert rendu_monnaie_centimes(700,700) == []
assert rendu_monnaie_centimes(112,500) == [200,100,50,20,10,5,2,1]