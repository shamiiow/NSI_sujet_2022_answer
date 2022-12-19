def rendu(money):
    list = [0, 0, 0]
    if money > 5:
        list[0] = money // 5
        money -= (money // 5)*5
    if money > 2:
        list[1] = money//2
        money -= (money//2)*2
    list[2] = money
    money -= money
    return list


assert rendu(13) == [2, 1, 1]
assert rendu(64) == [12, 2, 0]
assert rendu(89) == [17, 2, 0]

"""class Maillon :
    def __init__(self, v):
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self):
        maillon = self.dernier_file
        while maillon != ...:
            print(maillon.valeur)
            maillon = ...

    def defile(self) :
        if not self.est_vide():
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = Maillon()
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon
            maillon.suivant = None
            return resultat
        return None

F = File()
assert F.est_vide() == True
F.enfile(2)
assert F.affiche() == 2
assert F.est_vide() == False
F.enfile(5)
F.enfile(7)
assert F.affiche() == 752
assert F.defile() == 2
assert F.defile() == 5
assert F.affiche() == 7"""
