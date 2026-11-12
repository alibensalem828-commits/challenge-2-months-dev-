from random import random

class Personnage :

    def __init__(self, nom, vie_max,potions) :
        self.nom = nom
        self.vie_max = vie_max
        self.vie = vie_max
        self.potions=potions 
        

    def perdVie(self, n) :
        self.vie=self.vie - n
        if self.vie<0:
            self.vie=0

        print(self.nom + " perd " + str(n) + " pv " + self.etatPv())
    
    def gagneVie(self, n) :
        self.vie=self.vie + n
        if self.vie>self.vie_max :
            self.vie=self.vie_max
        print(self.nom + " gagne " + str(n) + " pv " + self.etatPv())
        
    def soigner(self):
        self.vie = self.vie_max
        print(self.nom + " est soigné(e) " + self.etatPv())

    def etatPv(self) :
        return "(Vie : " + str(self.vie) + "/" + str(self.vie_max) + ")"

    def decrire(self) :
        print("Nom : " + self.nom + " " + self.etatPv())
    def boirepotions(self):
        if self.potions>=1:
            if random()<0.8:
                self.soigner()
            else:
                self.perdVie(5)
            self.potions=self.potions-1

    def estmourant(self):
        return self.vie <= self.vie_max / 2
            
    def estmort(self):
        return self.vie==0
    def estvivant(self):
        return self.vie!=0



class Combat :

    def __init__(self, perso1, perso2) :
        self.perso1 = perso1
        self.perso2 = perso2
       # self.perdant=perdant
        #self.gagnant=gagnant

    def jouerRound(self) :
        if self.perso1.estmourant() :
            self.perso1.boirepotions()
        if self.perso2.estmourant() :
            self.perso2.boirepotions()
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
        while self.perso1.estvivant() and self.perso2.estvivant() :
            #while not self.perso1.estmort() and not self.perso2.estmort()
            self.jouerRound()
            #if self.perso1.estmourant() or self.perso2.estmourant():
             #           self.boirepotions()

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
    def gagnantperdant(self):
        #if self.perso2.vie() or self.perso1.vie() == 0:
        if self.perso1.estmort():
            print("")
            print("=============================================")
            print(self.perso1.nom)
            print("=============================================")
            print("")
        elif self.perso2.estmort():
            print("")
            print("=============================================")
            print(self.perso2.nom)
            print("=============================================")
            print("")
            
            
    def planifierCombats(self)


class Tournoi :
    def __init__(self,nom,inscrits,combats,):
        self.nom=nom
        self.inscrits=inscrits
        self.combats=combats

    def inscrire(self,personnage):

        self.inscrits.append(personnage)
    def planifierCombats(self):


    def planifierCombats(self) :
    n = len(self.inscrits)
    for i in range(n) :
        for j in range(???) :         # j commence où, d'après ta règle ?
            c = Combat(self.inscrits[???], self.inscrits[???])
            self.combats.???(c)
    














gollum = Personnage("Gollum", 10,3)
bilbo = Personnage("Bilbo", 15,2)
ali= Personnage('ali',20,4)
pavel=Personnage('pavel',32,0)
tournoi=Tournoi('superevent',[],[])
tournoi.inscrire(gollum)
tournoi.inscrire(bilbo)
tournoi.inscrire(ali)
tournoi.inscrire(pavel)


combat = Combat(gollum, bilbo)
#combat = Combat(ali,pavel)

combat.jouerCombat()
combat.gagnantperdant()
combat.etat()

combat.soignerPersonnages()
