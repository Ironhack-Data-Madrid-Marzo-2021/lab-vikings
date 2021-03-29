
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage = 1):
        self.health -= damage
    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def receiveDamage(self,damage = 1):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage = 1):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        return self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        return self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        strength_viking = random_viking.attack()
        damage_saxon = random_saxon.receiveDamage(strength_viking)

        if damage_saxon == "A Saxon has died in combat":
            self.saxonArmy.remove(random_saxon)
        return damage_saxon

    def saxonAttack(self):
        import random
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        strength_saxon = random_saxon.attack()
        damage_viking = random_viking.receiveDamage(strength_saxon)

       


    pass
