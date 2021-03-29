
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
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)

        damage_saxon = s.receiveDamage(v.attack())
        
        if s.health <= 0:
            self.saxonArmy.remove(s)

        return damage_saxon
            
    def saxonAttack(self):
        u = random.choice(self.vikingArmy)
        i = random.choice(self.saxonArmy)

        damage_viking = u.receiveDamage(i.attack())
        
        if u.health <= 0:
            self.vikingArmy.remove(u)
    
        return damage_viking

    def showStatus(self):

        if not self.saxonArmy:
            return "Vikings have won the war of the century!"

        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."        
        
        else:
            return "Vikings and Saxons are still in the thick of battle."