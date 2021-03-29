from vikingsClasses import Soldier,Viking,Saxon,War
import random

#creación Soldados
soldado_1 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_2 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_3 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_4 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_5 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_6 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_7 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_8 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_9 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_10 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_11 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_12 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_13 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_14 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_15 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_16 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_17 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_18 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_19 = Soldier(random.randint(1,50),random.randint(1,50))
soldado_20 = Soldier(random.randint(1,50),random.randint(1,50))

#creación equipos
team = War()
team.addViking(soldado_1)
team.addViking(soldado_2)
team.addViking(soldado_3)
team.addViking(soldado_4)
team.addViking(soldado_5)
team.addViking(soldado_6)
team.addViking(soldado_7)
team.addViking(soldado_8)
team.addViking(soldado_9)
team.addViking(soldado_10)
team.addSaxon(soldado_11)
team.addSaxon(soldado_12)
team.addSaxon(soldado_13)
team.addSaxon(soldado_14)
team.addSaxon(soldado_15)
team.addSaxon(soldado_16)
team.addSaxon(soldado_17)
team.addSaxon(soldado_18)
team.addSaxon(soldado_19)
team.addSaxon(soldado_20)

#no consigo hacer el juego con las clases creadas en War 

team_vikings_h = []
team_vikings_s = []

for vik in team.vikingArmy:
    team_vikings_h.append(vik.health)
    team_vikings_s.append(vik.strength)

team_saxons_h = []
team_saxons_s = []

for sax in team.saxonArmy:
    team_saxons_h.append(sax.health)
    team_saxons_s.append(sax.strength)

def vAttack(team_saxons_h, team_vikings_s):
        saxon_ = random.choice(team_saxons_h)
        viking_ = random.choice(team_vikings_s)
        saxon_ -= viking_
        
        for sax in team_saxons_h:
            if sax <= 0:
                team_saxons_h.remove(sax)

def sAttack(team_vikings_h, team_saxons_s):
        viking_ = random.choice(team_vikings_h)
        saxon_ = random.choice(team_saxons_s)
        viking_ -= saxon_
        
        for vik in team_vikings_h:
            if vik <= 0:
                team_vikings_h.remove(vik)
        
def showStatus_():
    if len(team_saxons_h) == 0:
        return print("Vikings have won the war of the century!")
    elif len(team_vikings_h) == 0:
        return print("Saxons have fought for their lives and survive another day...")
    else: 
        return print("Vikings and Saxons are still in the thick of battle.")

vAttack(team_saxons_h,team_vikings_s)
sAttack(team_vikings_h,team_saxons_s)
vAttack(team_saxons_h,team_vikings_s)
sAttack(team_vikings_h,team_saxons_s) 
vAttack(team_saxons_h,team_vikings_s)
sAttack(team_vikings_h,team_saxons_s)
vAttack(team_saxons_h,team_vikings_s)
sAttack(team_vikings_h,team_saxons_s)
sAttack(team_vikings_h,team_saxons_s)

showStatus_()


