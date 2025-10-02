class Creature: # Make subclasses for different types of creatures with unique behaviors
    def __init__(self, reproduction_rate:int, strength:int, lifespan:int):
        self.reproduction_rate = reproduction_rate
        self.strength = strength
        self.lifespan = lifespan
        self.age = 0
        self.characteristics = [self.reproduction_rate, self.strength, self.lifespan]
    
    def __str__(self):
        return str(self.strength)

    def __repr__(self):
        return self.__str__()
    
    def __getall__(self):
        return self.characteristics


