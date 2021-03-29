
import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage


# Viking

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

            
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage

        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"

        else:
            return f"A Saxon has died in combat" 
    

# War

class War():
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, name):
        if isinstance(name, Viking):
            self.vikingArmy.append(name)

    def addSaxon(self, name):
        if isinstance(name, Saxon):
            self.saxonArmy.append(name)

    def vikingAttack(self):
        viking_1 = random.choice(self.vikingArmy)
        saxon_1 = random.choice(self.saxonArmy)

        damage_saxon = saxon_1.receiveDamage(viking_1.attack())
        
        if saxon_1.health <= 0:
            self.saxonArmy.remove(saxon_1)

        return damage_saxon
            
    def saxonAttack(self):
        otro_vikingo = random.choice(self.vikingArmy)
        otro_saxon = random.choice(self.saxonArmy)

        damage_viking = otro_vikingo.receiveDamage(otro_saxon.attack())
        
        if otro_vikingo.health <= 0:
            self.vikingArmy.remove(otro_vikingo)
    
        return damage_viking

    def showStatus(self):

        if not self.saxonArmy:
            return "Vikings have won the war of the century!"

        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."        
        
        else:
            return "Vikings and Saxons are still in the thick of battle."