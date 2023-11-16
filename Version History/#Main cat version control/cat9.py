#
#cat2.py - Simulating the behavior of cats - Movement basics
#

from cat import Cat 
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#creating map
MAXROW = 30
MAXCOL = 30
CATNO = 3
STEPS = 6
#STEPS = int(input("Hours to simulate?"))

#Creating food and water sources
def sources():
    food = [(0,1),(0,0),(0,2),(0,3)]
    water = [(29,0),(29,1),(29,2),(29,3)]
    beds = [(3,29),(2,28),(1,27),(0,26)]
    boxes = [(14,15),(15,14),(14,14),(15,15)]
    return food, water, beds, boxes

#Movement basics
def movement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = r + random.choice(moves)
                cmoved = c + random.choice(moves)
                if rmoved < 0:
                    rmoved == 0
                if cmoved < 0:
                    cmoved == 0
                if rmoved == MAXROW:
                    rmoved = MAXROW - 1
                if cmoved == MAXCOL:
                    cmoved = MAXCOL - 1
                nextgrid[rmoved,cmoved] += 1
    return nextgrid

#Addons that make them more catlike
#Happiness
#Tiredness
#Hunger
#Thirst
#Sleep
#Differentiating passive and agressive
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

def map_feature(thing,colour):
    xlist = []
    ylist = []
    for row,col in thing:
        ylist.append(MAXROW - row - 1)
        xlist.append(col)
    plt.scatter(xlist,ylist,color=colour,marker='s')

def map_cat(CATNO, colour):
    xlist = []
    ylist = []
    slist = []
    for r in range(MAXROW):
        for c in range(MAXCOL):
            if CATNO[r,c] > 0:
                ylist.append(MAXROW - r - 1)
                xlist.append(c)
                slist.append(CATNO[r,c]*20)
    plt.scatter(xlist,ylist,s=slist,color=colour) 
def getImage(path):
    return OffsetImage(plt.imread(path))

def main():
    paths = [
            'cat.png']

    catmove = [-4,0,1]
    kittenmove = [-1,0,1]
    
    popgrid = np.zeros((MAXROW, MAXCOL), dtype=int)
    nextgrid = np.zeros((MAXROW, MAXCOL), dtype=int)
    catarrays = np.zeros((MAXROW, MAXCOL), dtype=int)
    kittenarrays = np.zeros((MAXROW, MAXCOL), dtype=int)
    happy = 100
    water, food, bed, boxes = sources()
    
    print("/nSimulating Cats/n")

    for i in range(CATNO):
        
        randR = random.randint(0,MAXROW-1)
        randC = random.randint(0,MAXCOL-1)
        catarrays[randR,randC] += 1
        plt.imshow(catarrays)
        print("cat at:[", randR, randC, "]")
    for x in range(STEPS):
        print("\n TIME:", x, "hours")
        catnext = movement(catarrays,catmove)
        kittennext = movement(kittenarrays,kittenmove)
        catarrays = catnext
        kittenarrays = kittennext
        happy = happy - 10
        print(happy)

        map_cat(kittenarrays, "r")
        #fed every 3 hours:
        if x%3 == 0:
            map_feature(water, "c")
            map_feature(food, "g")
        map_feature(bed, "k")
        map_feature(boxes, "w")
        plt.title("sda(time" + str(x) + "hours)")
        plt.xlim(-1,MAXCOL)
        plt.ylim(-1,MAXROW)
        plt.pause(0.5)
        plt.clf()
        plt.imshow(catarrays)

if __name__ == "__main__":
    main()
