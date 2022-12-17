def mini(t_moy, annees):
    i_min = 0
    for i in range(len(t_moy)):
        if t_moy[i] < t_moy[i_min]:
            i_min = i
    return t_moy[i_min], annees[i_min]

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

assert mini(t_moy, annees) == (12.5, 2016)


def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine
    
def est_nbre_palindrome(nbre):
    chaine = (inverse_chaine(str(nbre)))
    return est_palindrome(chaine)

assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True