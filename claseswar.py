import random
import time
import os
import sys
from IPython.display import clear_output

def introduce_numero ():
    
    """
    Ask user for a number
    
    Returns:
        int: selected number
    """
    
    while True:
        numero = input('Por favor introduce la opción deseada: ')
        if numero.isnumeric():
            numero = int(numero)
            return numero
            
        else:
            print ('debes introducir un valor adecuado')

def jugar_guerra (num_warriors):

    lista_cansancio_01 = ['a', 'b', 'c', 'd', 'e']
    lista_cansancio_02 = ['f', 'f', 'h', 'i', 'j']

    while len(lista_cansancio_01) > 0 and len(lista_cansancio_02) > 0: 
        guerra_01 = War(num_warriors)

        for x in range (self.num_warriors - 1):
            guerra_01.self.vikingArmy.append(lista_cansancio_01[x])
            guerra_01.self.saxon.saxonArmy.append(lista_cansancio_02[x])

        batallas = list(zip(lista_cansancio_01, lista_cansancio_02))

    
        for contador in range(len(batallas()) - 1):
            viking_index = 0

            guerra_01.self.saxon.receiveDamage(guerra_01.self.attack(batallas[contador][1]):)
            guerra_01.self.vikingo.receiveDamage(guerra_01.self.attack(batallas[contador][0):)
            contador += 1

        respuesta = return(guerra_01.self.showStatus())
        time.sleep(4)





def menu_opciones():
    
    opcion_menu = 0
    num_warriors = 3

    while opcion_menu == 1 or opcion_menu == 2 or opcion_menu == 3:

        print ('''

    ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
    ------------------⚔⚔⚔⚔⚔⚔-------------------
    -------------SELECCIONA TU GUERRA------------

    1.- La guerra que damos a los TA
    
    2.- Guerra de la inmutabilidad
    
    3.- Guerra del pepoloneso 8

    ---------------------------------------------
    ---------------------------------------------
    ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
    '''
            )

        # esta opción es para que en caso de que el usuario haya introducido un valor distinto a los del menú, llamarle la atención a ello
        #if opcion_menu != 0:
        #    print ('Tienes que introducir una opción válida') 
            
        opcion_menu = introduce_numero()

        if opcion_menu == 1:
            num_warriors = 3
            opcion_menu = 1
        
        elif opcion_menu == 2:
            num_warriors = 4
            opcion_menu = 2

        elif opcion_menu == 3:
            num_warriors = 4
            opcion_menu = 3

        else:
            clear_output()



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
    def __init__ (self, num_warriors):
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, nombre):
        self.vikingArmy.append(nombre)

    def addSaxon(self, nombre):
        self.saxonArmy.append(nombre)

    def vikingAttack(self):
        # eliges de la lista de saxon aleatoriamente uno para recibir el daño. Añadelo a un variable y te quitas de problemas
        # (existe un metodo llamado random.choice que hace esto mismo)
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
