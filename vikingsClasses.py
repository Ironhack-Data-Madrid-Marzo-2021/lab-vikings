
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

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage = 1):
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
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage = 1):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
    


    

# War


class War(Viking, Saxon):
    vikingArmy = []
    saxonArmy = []
    Saxon1 = Saxon().receiveDamage(self, health, strength, damage = 1)
    Vikings1 = Viking().receiveDamage(self, health, strength, damage = 1)

    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)

    def addViking(self, Viking = 10):
        self.vikingArmy += Viking

    def addSaxon(self, Saxon = 1):
        self.saxonArmy += Saxon
    
    def vikingAttack(self):
        x = (Saxon1 == Viking.attack(self.strength))
        Saxon1 += saxonArmy
        return x

    def saxonAttack(self):
        y = (Vikings1 == Saxon.attack(self.strength))
        Vikings1 += vikingArmy
        return y

    def showStatus(self):
        if saxonArmy == 0:
            return f"Vikings have won the war of the century!"
        elif vikingArmy == 0:
            return f"Saxons have fought for their lives and survive another day"
        else:
            return f"Vikings and Saxons are still in the thick of battle"
            
    

    



    

        


    
