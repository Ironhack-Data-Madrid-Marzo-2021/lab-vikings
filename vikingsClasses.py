
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        return


class Viking(Soldier): 
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"

#Funciona hasta el test 3 
import random

'''class War(Soldier):

    def __init__(self ):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self , Viking):
        self.viking = Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxon = Saxon
        self.saxonArmy.append(Saxon)
        
#no se como continuar
    
    def vikingAttack(self):
        random.choice(self.vikingArmy)
        random.choice(self.saxonArmy)

        if "A Saxon has died in combat":
            self.saxonArmy.remove(saxon)
            return 
   
    def saxonAttack(self):
        random.choice(self.vikingArmy)
        random.choice(self.saxonArmy)
        if f'Viking has died in act of combat' :
            self.vikingArmy.remove(Viking)
            return 
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."'''