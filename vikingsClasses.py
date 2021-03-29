
import random


# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__ (health, strength)
        self.name = name

    def receiveDamage(self, damage):
        
        self.health -= damage

        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        
        else:
            return f'{self.name} has received {damage} points of damage'

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__ (health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health <= 0:
            return f'A Saxon has died in combat'
        
        else:
            return f'A Saxon has received {damage} points of damage'



# War


class War:
    def __init__ (self):
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, nombre):
        self.vikingArmy.append(nombre)

    def addSaxon(self, nombre):
        self.saxonArmy.append(nombre)

    def vikingAttack(self):
        # eliges de la lista de saxon aleatoriamente uno para recibir el daño. Añadelo a un variable y te quitas de problemas
        saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        # eliges de la lista de vikingo aleatorimente uno para atacar. Añadelo a una variable y te quitas de problemas
        vikingo = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        # llamas al método receivedDamage (vikingo.attack)
        respuesta = saxon.receiveDamage (vikingo.attack())

        # limpias la lista de saxon en caso de que alguno tenga la vida a cero (comprehension)
        #if saxon.health <= 0:
        #    self.saxonArmy.remove(saxon)
        self.saxonArmy = [x for x in self.saxonArmy if x.health > 0]
        
        # llamas al método del objeto saxon receiveDamage(vikingo.attack) 
        return respuesta

    def saxonAttack(self):
        # eliges de la lista de vikingos aleatoriamente uno para recibir el daño.
        vikingo = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        
        # eliges de la lista de saxon uno aleatorimente para atacar.
        saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        # llamas al método receivedDamage (saxon.attack)
        respuesta = vikingo.receiveDamage (saxon.attack())

        # limpias la lista de saxon en caso de que alguno tenga la vida a cero (comprehension)
        self.vikingArmy = [x for x in self.vikingArmy if x.health > 0]
        
        # llamas al método del objeto saxon receiveDamage(vikingo.attack) 
        return respuesta

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        else:
            return "Vikings and Saxons are still in the thick of battle."
