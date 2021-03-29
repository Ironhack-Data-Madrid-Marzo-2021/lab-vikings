
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        return


'''# Viking
''class Viking(Soldier): 
    
    def __init__(name, health, strength):
        super().__init__(health, strength))
        self.name = name
        self.health = name
        self.strength = name

#class Viking:
    

# Saxon


#class Saxon:
    

# War


#class War:'''
    
