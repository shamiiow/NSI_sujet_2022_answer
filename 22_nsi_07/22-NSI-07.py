def conv_bin(n):
    list = []
    q = -1
    while q != 0:
        q = n//2
        list.append(n % 2)
        n = q
    return list[::-1]


assert conv_bin(9) == [1, 0, 0, 1]


def tri_bulles(T):
    n = len(T)
    for i in range(n-1, 0, -1):
        for j in range(i):

            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

print(tri_bulles([0, 5, 4, 8, 6, -5, 48, 5, 45, 7, 574, 54, 5, 7, 321, -68, -987, -65416, -897, -854, 547, 4798, 3521]))

