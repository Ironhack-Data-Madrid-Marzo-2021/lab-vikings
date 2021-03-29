
import math

# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= self.damage
    

# Viking

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name = name
    
    def attack(self):
        return self.strength

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
    def __init__(self, health, strength):
        super().__init__(health,strength)

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random
import array as arr
import numpy as np

class War():
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,viking):
        self.vikingArmy.append(viking)
        print(self.vikingArmy)
        
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        print(self.saxonArmy)

    def vikingAttack(self, vikingArmy, saxonArmy):
        some_viking_attacking = random.choice(saxonArmy)
        some_saxon_defending = random.choice(vikingArmy)

        some_viking_attacking