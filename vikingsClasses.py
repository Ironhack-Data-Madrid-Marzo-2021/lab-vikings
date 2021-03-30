
# Soldier 


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
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return self.name + "Has received" + str(damage) + "points of damage"
        else:
            return self.name + "has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

    

# Saxon


class Saxon(Soldier):

    def __init__(health,strength):
        super().__init__(health, strength)
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage # Esto creo que es asi pero no estoy seguro
        if self.health > 0:
            return "A Saxon has received" + str(damage) + "points of damage"
        else:
            return "A Saxon has died in combat"
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vikingo):
        if isinstance(vikingo, Viking):
            self.vikingArmy.append(vikingo)
    def addSaxon(self, sajon):
        if isinstance(sajon, Saxon):
            self.saxonArmy.append(sajon)
    def vikingAttack(self):
        ragnar = random.choice(self.vikingArmy)
        german = random.choice(self.saxonArmy)

        damage_saxon = german.receiveDamage(ragnar.attack())

        if german.health <= 0:
            self.saxonArmy.remove(german)

    def saxonAttack(self):
        ivar = random.choice(self.vikingArmy)
        germanico = random.choice(self.saxonArmy)

        damage_viking = ivar.receiveDamage(germanico.attack())
        
        if ivar.health <= 0:
            self.vikingArmy.remove(ivar)



    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fougth for their lives and survive another day"
        else:
            return "Vikings and Saxons are still in the thick of battle"
    
