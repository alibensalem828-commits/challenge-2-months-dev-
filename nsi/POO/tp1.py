from random import random

class Personnage :

    def __init__(self, nom, vie_max,potions,estmourant,estmort) :
        self.nom = nom
        self.vie_max = vie_max
        self.vie = vie_max
        self.potions=potions 
        self.mourant=estmourant 
        self.mort=estmort

    def perdVie(self, n) :
        if  self.vie - n<=0:
            self.vie=0

        print(self.nom + " perd " + str(n) + " pv " + self.etatPv())
    
    def gagneVie(self, n) :
        if self.vie + n >= max(self.vie):
            self.vie=self.vie_max
        print(self.nom + " gagne " + str(n) + " pv " + self.etatPv())
        
    def soigner(self) :
        self.vie = self.vie_max
        print(self.nom + " est soigné(e) " + self.etatPv())

    def etatPv(self) :
        return "(Vie : " + str(self.vie) + "/" + str(self.vie_max) + ")"

    def decrire(self) :
        print("Nom : " + self.nom + " " + self.etatPv())
    #def boirepotions(self):
        #if self.potions>=1:#

    def estmourant(self):
        if self.vie =< self.vie%2:
            return True
        else: 
            return False
    def estmort(self):
        if self.vie=0:
            return True
        else:
            return False



class Combat :

    def __init__(self, perso1, perso2) :
        self.perso1 = perso1
        self.perso2 = perso2

    def jouerRound(self) :
        # random() retourne un nombre aléatoire entre 0 et 1
        # donc la ligne ci-dessous équivaut à dire "une fois sur deux" :
        if random() > 0.5 :
            self.perso1.perdVie(1)
        else :
            self.perso2.perdVie(1)
    
    def jouerCombat(self) :

        print("")
        print("=============================================")
        print("Début du combat : " + self.perso1.nom + " vs " + self.perso2.nom)
        print("=============================================")
        print("")        

        # Le combat se déroule en 15 rounds
        for i in range(15) :
            self.jouerRound()

        print("")
        print("=============================================")
        print("Combat terminé !")
        print("=============================================")
        print("")

    def soignerPersonnages(self) :
        print("")
        self.perso1.soigner()
        self.perso2.soigner()
    
    def etat(self) :
        print("")
        print('État des personnages :')
        self.perso1.decrire()
        self.perso2.decrire()

gollum = Personnage("Gollum", 10)
bilbo = Personnage("Bilbo", 15)

combat = Combat(gollum, bilbo)

combat.jouerCombat()

combat.etat()

combat.soignerPersonnages()