#
#cat.py - definitions 
#

class Cat():
    def __init__(self,name,age,stage,passive,hunger,thirst,happiness,tiredness):
        self.name = name
        self.age = age
        self.stage = stage
        self.passive = passive
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness
        self.tiredness = tiredness

    def names(self, names):
        self.name.append(names)

    #defining what makes them cats or kittens :D
    def stage(self,age):
        if age < 12:
            stage = "Kitten"
        else:
            stage = "Cat"
