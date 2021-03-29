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
        super().__init__(health, strength) # éstos atributos ya entan en Soldier
        self.name = name # éste nuevo atributo es propio de Viking
 
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return f"Odin Owns You All!"
   

# Saxon

class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength) # éstos atributos ya entan en Soldier

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        return f"A Saxon has died in combat"


# War

class War:

    def __init__(self):
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

 #   def addVikingFromScratch(self, health, strength, name):
 #       self.vikingArmy.append(Viking(name, health, strength))

 #   def addSaxonFromScratch(self, health, strength):
 #       self.saxonArmy.append(Saxon(health, strength))

    def vikingAttack(self):
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        
        result = chosen_saxon.receiveDamage(chosen_viking.strength)    

        if chosen_saxon.health <= 0:
            self.saxonArmy.remove(chosen_saxon)
        
        return result

    def saxonAttack(self):
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        
        result = chosen_viking.receiveDamage(chosen_saxon.strength)    

        if chosen_viking.health <= 0:
            self.vikingArmy.remove(chosen_viking)
        
        return result


    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        return f"Vikings and Saxons are still in the thick of battle."





        
       




  
