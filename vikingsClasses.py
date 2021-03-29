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

    def receiveDamage(self, damage):
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

    def addViking(self, viking_1):
        self.vikingArmy.append(viking_1)

    def addSaxon(self, saxon_1):
        self.saxonArmy.append(saxon_1)

    def vikingAttack(self):
        rnd_saxon = random.choice(self.saxonArmy)
        rnd_viking = random.choice(self.vikingArmy)
        result = rnd_saxon.receiveDamage(rnd_viking.strength)
        if rnd_saxon.health <= 0:
            self.saxonArmy.remove(rnd_saxon)
        return result

    def saxonAttack(self):
        rnd_viking = random.choice(self.vikingArmy)
        rnd_saxon = random.choice(self.saxonArmy)
        result = rnd_viking.receiveDamage(rnd_saxon.strength)
        if rnd_viking.health <= 0:
            self.vikingArmy.remove(rnd_viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
