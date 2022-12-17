def nb_repetitions(n, list):
    rep = 0
    for i in range(len(list)):
        if list[i] == n:
            rep += 1
    return rep

assert nb_repetitions(5,[2,5,3,5,6,9,5]) == 3
assert nb_repetitions('A',['B','A','B','A','R']) == 2
assert nb_repetitions(12,[1,'!',7,21,36,44]) == 0

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

assert binaire(0) == '0'
assert binaire(77) == '1001101'
