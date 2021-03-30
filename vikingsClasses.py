
# Soldier

import random as rd

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
    def __init__(self, name, health, strength):
        super().__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if health > 0:
            return self.name + f" has received {damage} points of damage"
        else:
            return self.name + f" has died in act of combat"

    def battleCry(self):
        return f"Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(self, health, strength)


    def receiveDamage(damage):
        self.health = self.health - damage
        if health >0:
            return f" A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []   

    def addViking(self, Viking):
        self.vikingArmy.append(vik)



    def addSaxon(self, Saxon):
        self.saxonArmy.append(sax)

    
    def vikingAttack(self):
        vikSoldier = rd.choice(self.vikingArmy)
        saxSoldier = rd.choice(self.saxonArmy)

        damage_saxon = saxSoldier.receiveDamage(vikSoldier.attack())

        if saxon.health <=0:
            self.saxonArmy.remove(saxSoldier)

        return damage_saxon


    def saxonAttack(self):
        vikSoldier_2 = rd.choice(self.vikingArmy)
        saxSoldier_2 = rd.choice(self.saxonArmy)

        damage_viking = saxSoldier_2.receiveDamage(vikSoldier_2.attack())

        if saxon.health <=0:
            self.saxonArmy.remove(vikSoldier_2)

        return damage_viking


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."

    

