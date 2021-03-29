
from random import choice as elige
from time import  sleep
class Soldier:
    def __init__ (self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health-=damage

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        self.health = health
        self.strength = strength
   
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0 :            
            return(f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")

    
    def battleCry(self):
        return ("Odin Owns You All!")

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health-=int(damage)
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return "A Saxon has died in combat"

class War(Soldier):
    def __init__(self):
        self.vikingArmy=list()
        self.saxonArmy=list()
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)  
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        herido = elige(self.saxonArmy)
        atacante = elige(self.vikingArmy)
        mensaje=herido.receiveDamage(atacante.attack())
        
        if mensaje == 'A Saxon has died in combat':
            self.saxonArmy.remove(herido)   
        return mensaje

    def saxonAttack(self):
        herido = elige(self.vikingArmy)
        atacante = elige(self.saxonArmy)
        mensaje = herido.receiveDamage(atacante.attack())

        if mensaje == f"{herido.name} has died in act of combat":
            self.vikingArmy.remove(herido)  
        return mensaje

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == [] :

            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


guerra=War()

guerra.addSaxon(Saxon(10,3))
guerra.addViking(Viking("Perdr",2,9))
guerra.addSaxon(Saxon(4,7))
guerra.addViking(Viking("Pablo",2,9))
guerra.addSaxon(Saxon(10,3))
guerra.addViking(Viking("Thor", 8,7))
guerra.addSaxon(Saxon(2,10))
guerra.addViking(Viking("Vicky", 6,6))
guerra.addSaxon(Saxon(10,3))
guerra.addViking(Viking("Olaf", 7,5))
guerra.addSaxon(Saxon(10,10))
guerra.addViking(Viking("Luther", 10,1))
guerra.addSaxon(Saxon(10,3))
guerra.addViking(Viking("Haffman", 16,10))
guerra.addSaxon(Saxon(10,3))
guerra.addViking(Viking("Sinjan", 2,1))

while True:
    print(str(guerra.vikingAttack()))
    print(guerra.showStatus())

    if guerra.showStatus() !="Vikings and Saxons are still in the thick of battle.":
        break

    print(str(guerra.saxonAttack()))
    print(guerra.showStatus())

    if guerra.showStatus() !="Vikings and Saxons are still in the thick of battle.":
        break
    
   



