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
        nouveau_maillon = Maillon(...)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = ...

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != ... :
            print(maillon.valeur)
            maillon = ...

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = ...
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = ...
            maillon.suivant = None
            return resultat
        return None
"""