#
#cat1.py - Simulating the behavior of cats
#

from cat import Cat 
import random
import numpy as np
import matplotlib.pyplot as plt

#print statement for the individual cats information
def information():
    print('\nCat info\n')
    for i in range(len(population)):
        print("Name: ", population[i].name, "\nAge: ", population[i].age, "\nPassive: ", population[i].passive,"\nStage: ", population[i].stage, "\nHunger:", population[i].hunger, "\nthirst",population[i].thirst, "\ntiredness", population[i].tiredness, "\nhappiness", population[i].happiness)
        print("\n")
population = []

#print("How many cats do you want?")

#trying to get the user to input a name and age for the simulation
#abandoned after trying and failing multiple times
#namelist = {}
#agelist = {}
#passivity = {}
#cat1337 = {}
#population = int(input("Number of cats: "))
#for i in range(population):
#    if population < 4:
#        namelist["name%s" %i] = input("name ")
#        agelist["age%s" %i] = input("age ")
#        passivity["passive%s" %i] = bool(input("Is the passive?"))
#    else:
#        print("Too many cats, try again")
#        population = int(input())
#print(namelist)
#print(agelist)
#print(passivity)

#for i in range(population):
#    cat1337["cat%s" %i] = print(namelist[i], agelist[i], passivity[i])

cat1 = Cat("Cindy", 12, "kitten", True , 0, 0, 100, 0)
cat2 = Cat("Gerald", 46, "cat",  False, 0, 0, 100, 0)
cat3 = Cat("Mindy", "32", "cat",  True , 0, 0, 100, 0)
population = [cat1,cat2,cat3]
information()
