
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health = self.health - damage 

# Viking

class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def receiveDamage(self, damage):
            self.health = self.health - damage
            if self.health > 0:
                return f"A Saxon has received {damage} points of damage"
            else:
                return f"A Saxon has died in combat"

# War

import random
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        return self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        return self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)
        battle = randomSaxon.receiveDamage(randomViking.strength)
        if randomSaxon.health <= 0:
            self.saxonArmy.remove(randomSaxon)
        return battle
    def saxonAttack(self):
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)
        battle = randomViking.receiveDamage(randomSaxon.strength)
        if randomViking.health <= 0:
            self.vikingArmy.remove(randomViking)
        return battle
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:  
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:  
            return "Vikings and Saxons are still in the thick of battle."
    
