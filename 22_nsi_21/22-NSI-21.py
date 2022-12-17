def multiplication(n1, n2):
    resultat = 0
    if n2 < 0 and n1 < 0:
        for i in range(abs(n2)):
            resultat += abs(n1)
        return resultat
    for i in range(abs(n2)):
        resultat += n1
    return resultat

assert multiplication(3,5) == 15
assert multiplication(-4,-8) == 32
assert multiplication(-2,6) == -12
assert multiplication(-2,0) == 0

def dichotomie(tab, x):
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return False
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False