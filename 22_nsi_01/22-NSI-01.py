def recherche(caractere, mot):
    ocurrence = 0
    for i in range(len(mot)):
        if mot[i] == caractere:
            ocurrence += 1
    return ocurrence

assert recherche('e', "sciences") == 2
assert recherche('i',"mississippi") == 4
assert recherche('a',"mississippi") == 0



Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
       return solution
    p = Pieces[i]
    if p <= arendre:
        solution.append(Pieces[i])
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

assert rendu_glouton(68,[],0) == [50, 10, 5, 2, 1]
assert rendu_glouton(291,[],0) == [100, 100, 50, 20, 20, 1]