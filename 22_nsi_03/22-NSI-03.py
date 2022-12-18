def delta(tab):
    delta_tab = [tab[0]]
    for i in range(1, len(tab)):
        delta_tab.append(tab[i]-tab[i-1])
    return delta_tab

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]

class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ...
    if e.gauche is not None:
        s = s + expression_infixe(...)
    s = s + ...
    if ... is not None:
        s = s + ...
    if ...:
        return s
    
    return '('+ s +')'

