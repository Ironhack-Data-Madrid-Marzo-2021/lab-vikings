
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage



    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strenght):
        self.name = name
        super().__init__(health, strenght)
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        else:
            return f'{self.name} has received {self.damage} points of damage'


    def battleCry(self):
        return "Odin Owns You All!"

    
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return f"A Saxon has received {self.damage} points of damage"

    pass

# War

import random 

class War:
    def __init__(self):
       self.vikingArmy = []
       self.saxonArmy =  []

    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        fighter = random.choice(self.vikingArmy)

        defender = random.choice(self.saxonArmy)

        message = defender.receiveDamage(fighter.attack())

        if "A Saxon has died in combat" == message:
          self.saxonArmy.remove(defender)

        return message

    def saxonAttack(self):
        defender1 = random.choice(self.vikingArmy)
        fighter1 = random.choice(self.saxonArmy)

        message1 = defender1.receiveDamage(fighter1.attack())
        if f'{defender1.name} has died in act of combat' == message1:
            self.vikingArmy.remove(defender1)
        return message1

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."










    pass
