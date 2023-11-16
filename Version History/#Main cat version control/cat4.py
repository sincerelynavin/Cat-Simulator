#
#cat2.py - Simulating the behavior of cats - Movement basics
#

from cat import Cat 
import random
import numpy as np
import matplotlib.pyplot as plt

#creating map
MAXROW = 25
MAXCOL = 25
CATNO = 3
STEPS = 25

#Creating food and water sources
def sources():
    food = []
    water = []

#extras
def extras():
    beds = []
    boxes = []

#Dynamic food sources
#Differentiating passive and agressive
#Movement basics
#def movement(current, moves):
#    nextgrid = np.zeros(current.shape, dtype="int")
    
#    for row in range(MAXROW):
#        for col in range(MAXCOL):
#            for x in range(current[row,col]):
#                nextrow = row + random.choice(moves)
#                nextcol = col + random.choice(moves)
#                #To not obtain positive values:
#                if nextrow < 0:
#                    nextrow = 0
#                if nextcol < 0:
#                    nextcol = 0
#                #To keep the cats within the boundary:
#                if nextrow >= MAXROW:
#                    nextrow = MAXROW - 1
#                if nextcol >= MAXCOL:
#                    nextcol = MAXCOL - 1
#                nextgrid[nextrow, nextcol] += 1
#    return nextgrid


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

def main():

    catmove = [-4,0,1]
    kittenmove = [-1,0,1]
    print("/nSimulating Cats/n")
    popgrid = np.zeros((MAXROW, MAXCOL), dtype=int)
    nextgrid = np.zeros((MAXROW, MAXCOL), dtype=int)

    for i in range(CATNO):
        randR = random.randint(0,MAXROW-1)
        randC = random.randint(0,MAXCOL-1)
        popgrid[randR,randC] += 1
        print("cat at:[", randR, randC, "]")

    print("\nINTIAL POPULATION\n")
    plt.cla()
    plt.imshow(popgrid)
    plt.pause(0.5)

    for x in range(STEPS):
        print("\n TIME:", x, "hours")

        nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
        for r in range(MAXROW):
            for c in range(MAXCOL):
                for i in range(popgrid[r,c]):
                    rmoved = r + random.choice([-3,0,1])
                    cmoved = c + random.choice([-3,0,1])
                    if rmoved < 0:
                        rmoved == 0
                    if cmoved < 0:
                        cmoved == 0
                    if rmoved == MAXROW:
                        rmoved = MAXROW - 1
                    if cmoved == MAXCOL:
                        cmoved = MAXCOL - 1
                    nextgrid[rmoved,cmoved] += 1 

        popgrid = nextgrid       
        plt.cla()
        plt.title("CATSIM (Time = " +str(x) + "hours)")
        plt.imshow(popgrid)
        plt.pause(0.5)
       
if __name__ == "__main__":
    main()
