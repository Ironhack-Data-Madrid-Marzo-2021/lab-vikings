import random
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage 
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        if self.health <= 0:
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
        if self.health <= 0:
            return f"A Saxon has died in combat"


# War

class War:
    vikingArmy = []
    saxonArmy = [""]
    random_saxon = random.choice(saxonArmy)
    def __init__(self.):
        self.vikingArmy = []
        self.saxonArmy = []
        
    
    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(self.Viking)
    
    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(self.Saxon)
    
    def vikingAttack(self):
        self.random_viking = random.choice(self.vikingArmy)
        self.health -= self.strength
        if self.health <= 0:
            self.saxonArmy.remove(self.random_saxon)
            return f"{self.random_saxon} have died"
        if self.health(self.random_saxon) > 0:
            return random_saxon.receiveDamage(Saxon) 
            
    def saxonAttack(self):
        self.random_viking = random.choice(self.vikingArmy)
        self.random_saxon = random.choice(self.saxonArmy)
        self.health -= self.strength
        if self.health <= 0:
            self.vikingArmy.remove(self.random_viking)
            return f"{self.random_viking} have died"
        if self.health(self.random_viking) > 0:
            return random_saxon.receiveDamage(viking) 

    def showStatus(self):
        if len.saxonArmy == 0:
            return "Vikings have won the war of the century!"
        if len.vikingArmy == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len.saxonArmy == 1 and len.vikingArmy == 1:
            return "Vikings and Saxons are still in the thick of battle."