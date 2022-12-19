def recherche(k, list):
    i_search = -1
    for i in range(len(list)):
        if list[i] == k:
            i_search = i
    return i_search


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5


class AdresseIP:

    def __init__(self, adresse):

        self.adresse = adresse
   
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]
        
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           réservée, False sinon"""
        return AdresseIP.liste_octet(self) == [192, 168, 0, 0] or AdresseIP.liste_octet(self) == [192, 168, 0, 255]
             
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l’adresse self
           si elle existe et False sinon"""
        if AdresseIP.liste_octet(self)[3] < 254:
            octet_nouveau = AdresseIP.liste_octet(self)[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')

assert adresse1.est_reservee() == False
assert adresse3.est_reservee() == True
assert adresse2.adresse_suivante().adresse == '192.168.0.3'
