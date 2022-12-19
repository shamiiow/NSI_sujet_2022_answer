def convertir(list):
    dec = 0
    i = 0
    exp = len(list) - 1
    while i < len(list):
        dec += (2**(exp-i))*list[i]
        i += 1
    return dec

assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83

def tri_insertion(L):
    n = len(L)
    if n == 0:
        return L
    for j in range(1, n):
        e = L[j]
        i = j
        while 0 < i and (L[i-1] > L[j]):
            i = i - 1
        if i != j:
            for k in range(j,i,-1):
                L[k] = L[k-1]
            L[i] = e
    return L


assert tri_insertion([2,5,-1,7,0,28]) == [-1, 0, 2, 5, 7, 28]
assert tri_insertion([10,9,8,7,6,5,4,3,2,1,0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
