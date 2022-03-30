import random
import string

class Robot:
    name_re = list()
    
    
    def __init__(self):
        self.name = self.generate_name()


    def reset(self):
        self.name = self.generate_name()


    def generate_name(self):
        name = self.rand_name()
        while name in self.name_re:
            name = self.rand_name()
        self.name_re.append(name)
        return name


    def rand_name(self):
        return random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(100, 999))
        
        