def maxi(list):
    i_max = 0
    for i in range(len(list)):
        if list[i] > list[i_max]:
            i_max = i
    return (list[i_max], i_max)

assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9,3)


def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < len(seq_adn) and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j +=1
        if j == g:
            trouve = True
        i += 1
    return trouve
assert recherche("AATC", "GTACAAATCTTGCC") == True
assert recherche("AGTC", "GTACAAATCTTGCC") == False