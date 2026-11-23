class Cellule :
    def __init__(self,val,next):
        self.valeur=val
        self.suivante=next
#avec while :
def longueur(liste):
    i=0
    while liste is  not None:
        i+=1
        liste=liste.suivante
    return i

#pour le eniem reccursiviter:
def nieme_element(n,liste):
    if  liste is None:
        raise IndexError('indince invalide')
    if n==0:
        return liste.valeur 
    else:
        return nieme_element(n-1,liste.suivante)
