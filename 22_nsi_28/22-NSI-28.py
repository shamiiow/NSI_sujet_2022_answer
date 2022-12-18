def moyenne(tab):
    m = 0
    for i in range(len(tab)):
        m += tab[i]
    return m / len(tab)

assert moyenne([1.0]) == 1.0
assert moyenne([1.0,2.0,4.0]) == 2.3333333333333335

def dec_to_bin(a):
    bin_a = str(a%2)
    a = a//2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

assert dec_to_bin(83) == '1010011'
assert dec_to_bin(127) == '1111111'