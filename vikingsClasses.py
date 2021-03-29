
# Soldier


class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return(self.strength)

    def receiveDamage(self, damage):
    
        self.health -= damage
        print(self.health)




# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

       
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

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
       
    def attack (self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War

import random

class War:
    
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        if isinstance(vik, Viking):
            self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        if isinstance(sax, Saxon):
            self.saxonArmy.append(sax)

    def vikingAttack(self):
        s_warrior = random.choice(self.saxonArmy) 
        v_warrior = random.choice(self.vikingArmy)

        d_saxon = s_warrior.receiveDamage(v_warrior.attack())

        if s_warrior.health <= 0:
            self.saxonArmy.remove(s_warrior)

        return d_saxon

    def saxonAttack(self):
        sa_warrior = random.choice(self.saxonArmy) 
        vi_warrior = random.choice(self.vikingArmy) 

        d_vikin = vi_warrior.receiveDamage(sa_warrior.attack())

        if vi_warrior.health <= 0:
            self.vikingArmy.remove(vi_warrior)

        return d_vikin



    def showStatus(self):
        if len(self.saxonArmy) is 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) is 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    