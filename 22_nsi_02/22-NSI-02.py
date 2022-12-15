def moyenne(list):
    up = 0
    down = 0
    for i in range(len(list)):
        up += list[i][0] * list[i][1]
        down += list[i][1]
    return up/down
assert moyenne([(15,2),(9,1),(12,3)]) == 12.5


def pascal(n):
    C = [[1]]
    for k in range(1, n+1):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]