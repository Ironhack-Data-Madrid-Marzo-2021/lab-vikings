
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return(self.strength)

    def receiveDamage(self,damage):
        self.health -= damage
        print(self.health)



# Viking
class Viking(Soldier):
    def __init__(self,name,health, strenght):
        super().__init__(health,strenght)
        self.name = name
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!" 

# Saxon
class Saxon(Soldier):
    
    def __init__(self,health, strenght):
        super().__init__(health,strenght)
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return f"A Saxon has died in combat"

# War

import random

class War:

    def __init__ (self):
       self.vikingArmy = []
       self.saxonArmy = []
        
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        saxon_ = random.choice(self.saxonArmy)
        viking_ = random.choice(self.vikingArmy)
        vattack = saxon_.receiveDamage(viking_.strength) 
        
        for sax in self.saxonArmy:
            if sax.health <= 0:
                self.saxonArmy.remove(sax)
        
        return f"{vattack}"
        
    def saxonAttack(self):
        saxon_ = random.choice(self.saxonArmy)
        viking_ = random.choice(self.vikingArmy)
        sattack = viking_.receiveDamage(saxon_.strength) 
        
        for vik in self.vikingArmy:
            if vik.health <= 0:
                self.vikingArmy.remove(vik)
        
        return f"{sattack}"
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else: 
            return "Vikings and Saxons are still in the thick of battle."
