import random as rd
class Soldier:

    def __init__ (self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage


class Viking(Soldier):

    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return (f"{self.name} has received {damage} points of damage")
        elif self.health<=0:
                return (f"{self.name} has died in act of combat") 
    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super(). __init__(health, strength )
    def receiveDamage(self, damage):
            self.health-=damage
            if self.health>0:
                return (f"A Saxon has received {damage} points of damage")
            elif self.health <=0 :
                    return (f"A Saxon has died in combat")

class War():
    def __init__(self):
     self.vikingArmy=[]
     self.saxonArmy=[]
    
    def addViking (self,soldado):
        self.vikingArmy.append (soldado)

    def addSaxon(self,soldado):
        self.saxonArmy.append (soldado)

    def vikingAttack(self):
        saxon=rd.choice (self.saxonArmy)
        viking=rd.choice (self.vikingArmy)

        combate= saxon.receiveDamage (viking.attack())
        for soldado in self.saxonArmy:
            if soldado.health<=0:
                self.saxonArmy.remove (soldado)
        return combate

    def saxonAttack(self):
        saxon=rd.choice (self.saxonArmy)
        viking=rd.choice (self.vikingArmy)

        combate= viking.receiveDamage (saxon.attack())
        for soldado in self.vikingArmy:
            if soldado.health<=0:
                self.vikingArmy.remove (soldado)
        return combate

    def showStatus(self):
        if len (self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len (self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
