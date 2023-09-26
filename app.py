class Person:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    def afficheNom(self):
        print('Hello '+self.name)

class Etudiant(Person):
    def __init__(self,nm,ag,nt):
        Person.__init__(self,nm,ag)
        self.note=nt
    def afficher(self):
        super().afficheNom()
    
class Professor(Person):
    def __init__(self,nm,ag,sl):
        Person.__init__(self,nm,ag)
        self.salaire=sl
    def afficher(self):
        super().afficheNom()
etd1=Etudiant('manar',20,14)
prof=Professor('samir',32,10000)

#prof.afficheNom()
#etd1.afficheNom()
etd1.afficher()
prof.afficher()