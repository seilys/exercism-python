from random import randint
from math import floor

class Character:
    def __init__(self):
        self.strength = self.sum_result()
        self.dexterity = self.sum_result()
        self.constitution = self.sum_result()
        self.intelligence = self.sum_result()
        self.wisdom = self.sum_result()
        self.charisma = self.sum_result()
        self.hitpoints = 10 + modifier(self.constitution)
        
    
    def ability(self):
        return self.sum_result();
    
        
    def sum_result(self):
        numbers = list()
        [numbers.append(randint(1,6)) for i in range(0,4)]
        return (sum(numbers) - min(numbers))
    
    
def modifier(number):
    return floor((number-10) / 2)
        