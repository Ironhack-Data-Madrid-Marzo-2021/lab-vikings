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
    def receiveDamage(self,damage):
        self.damage = damage 
        self.health = self.health - self.damage
        if self.health > 0: 
            return f"{self.name} was dealt {self.damage} damage"
        if self.health <= 0:
            return f"{self.name} honorably died in combat." 
    def battleCry(self): 
        return "Odin Owns You All!"  
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} damage"
        if self.health <= 0:
            return f"A Saxon honorably died in combat." 

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = saxon.receiveDamage(viking.attack())
    
