#
#cat2.py - Simulating the behavior of cats - Couldnt simulate both cats and kittens in the same thing :(
#

from cat import Cat 
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#age1 = int(input("How old is your first cat?"))

#creating map
MAXROW = 30
MAXCOL = 30

#NO = int(input("How many cats to simulate?"))
#for i in range(NO):
#    age = int(input("Age of cat: "))
#    print(age)
#CATNO = int(input("how many cats to simulate?"))
#if CATNO > 7:
#    print("too many cats :(")
#    CATNO = int(input("how many cats to simulate?"))
CATNO = 2
KITTENNO = 2
STEPS = 15 
#STEPS = int(input("Hours to simulate?"))

#Reading file
def readlists(filelist):
    externallist = [(int(l.split(",")[0]),int(l.split(",")[1])) for l in filelist[1:]]
    return externallist

#Creating food and water sources
def sources(files):
    fileobj = open('terrain.txt', 'r')
    externalnew = fileobj.readlines()
    fileobj.close()

    food = readlists(externalnew[0].strip().split(':'))
    water = readlists(externalnew[1].strip().split(':'))
    beds = readlists(externalnew[2].strip().split(':'))
    boxes = readlists(externalnew[3].strip().split(':'))
    boundary = readlists(externalnew[4].strip().split(':'))
    return food, water, beds, boxes, boundary

#Movement - base
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

#Movement = happiness
def hmovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 14
                cmoved = 16
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#Movement = tired
def tmovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 4 
                cmoved = 29
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#Movement = hunger
def hunmovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 1
                cmoved = 1
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#Movement = thirst
def thimovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 29
                cmoved = 1
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#Addons that make them more catlike
#Differentiating passive and agressive

#print statement for the individual cats information
#def information():
#    print('\nCat info\n')
#    for i in range(len(population)):
#        print("Name: ", population[i].name, "\nAge: ", population[i].age, "\nPassive: ", population[i].passive,"\nStage: ", population[i].stage, "\nHunger:", population[i].hunger, "\nthirst",population[i].thirst, "\ntiredness", population[i].tiredness, "\nhappiness", population[i].happiness)
#        print("\n")
#population = []
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

#cat1 = Cat("Cindy", 12, "kitten", True , 0, 0, 100, 0)
#cat2 = Cat("Gerald", 46, "cat",  False, 0, 0, 100, 0)
#cat3 = Cat("Mindy", "32", "cat",  True , 0, 0, 100, 0)
#population = [cat1,cat2,cat3]
#information()

def map_feature(thing,colour):
    xlist = []
    ylist = []
    for row,col in thing:
        ylist.append(MAXROW - row - 1)
        xlist.append(col)
    plt.scatter(xlist,ylist,color=colour,marker='s')

def getImage1(path):
    return OffsetImage(plt.imread(path, format="png"), zoom=0.15)
def getImage2(path):
    return OffsetImage(plt.imread(path, format="png"), zoom=0.05)

def map_kitten(KITTENNO,colour):
    paths = ['cat3.png','cat3.png','cat3.png','cat3.png']
    xlist = []
    ylist = []
    slist = []
    for r in range(MAXROW):
        for c in range(MAXCOL):
            if KITTENNO[r,c] > 0:
                ylist.append(MAXROW - r - 1)
                xlist.append(c)
                slist.append(KITTENNO[r,c]*20)
#    fig, ax = plt.subplots()
#    ax.scatter(xlist,ylist,s=slist)
#    for xlist, ylist, path in zip(xlist, ylist, paths):
#        ab = AnnotationBbox(getImage1(path), (xlist,ylist), frameon=False)
#        ax.add_artist(ab)
    plt.scatter(xlist,ylist,s=slist,color=colour)        
def map_cat(CATNO,colour):
    paths = ['cat2.png','cat2.png','cat2.png','cat2.png']
    xlist = []
    ylist = []
    slist = []
    for r in range(MAXROW):
        for c in range(MAXCOL):
            if CATNO[r,c] > 0:
                ylist.append(MAXROW - r - 1)
                xlist.append(c)
                slist.append(CATNO[r,c]*20)
    #fig, ax = plt.subplots()
    #ax.scatter(xlist,ylist,s=slist)
    #for xlist, ylist, path in zip(xlist, ylist, paths):
    #    ab = AnnotationBbox(getImage2(path), (xlist,ylist), frameon=False)
    #    ax.add_artist(ab)
    plt.scatter(xlist,ylist,s=slist,color=colour)

def main():
    #Happiness
    cathappy = 100
    kittenhappy = 100
    
    #Tiredness
    cattiredness = 0
    kittentiredness = 0
    
    #Hunger
    cathungry = 0
    kittenhungry = 0

    #Thirst
    catthirst = 0
    kittenthirst = 0

    #Moving amount
    catmove = [-3,0,1]
    kittenmove = [-2,0,1]
    
    #Basic arrays
    nextgrid = np.zeros((MAXROW, MAXCOL), dtype=int)
    catarrays = np.zeros((MAXROW, MAXCOL), dtype=int)
    kittenarrays = np.zeros((MAXROW, MAXCOL), dtype=int)
    water, food, bed, boxes, boundary = sources("terrain.txt")
    
    print("/nSimulating Cats/n")

    for i in range(CATNO):
        
        randR = random.randint(0,MAXROW-1)
        randC = random.randint(0,MAXCOL-1)
        catarrays[randR,randC] += 1
        print("cat at:[", randR, randC, "]")
    
    for i in range(KITTENNO):
        
        randR = random.randint(0,MAXROW-1)
        randC = random.randint(0,MAXCOL-1)
        kittenarrays[randR,randC] += 1
        print("kitten at :[:", randR, randC, "]")

    for x in range(STEPS):
        #print statements:
        print('\n')
        print("TIME:", x, "hours")
        print('\n')
        #Cat print statements:
        print("Cat info:")
        print("How tired are the cats: ", cattiredness)
        
        #Kitten print statements:
        print("Kitten info:")
        print("How tired are the kittens: ", kittentiredness)

        #Normal cat behavior
        catnext = movement(catarrays,catmove)
        kittennext = movement(kittenarrays,kittenmove)

        #Normal kitten behavior
        catarrays = catnext
        kittenarrays = kittennext

        #Cat behaviors:

        #Are the cats tired?
        cattiredness = cattiredness + 5
        if cattiredness > 60:
            tiredcat = tmovement(catarrays,catmove)
            catarrays = tiredcat
            #print("cat slept")
            cattiredness = 0
        
        #Are the cats happy?
        cattiredness = cattiredness + 5
        if cattiredness > 60:
            tiredcat = tmovement(catarrays,catmove)
            catarrays = tiredcat
            #print("cat slept")
            cattiredness = 0
        
        #Are the cats tired?
        cattiredness = cattiredness + 5
        if cattiredness > 60:
            tiredcat = tmovement(catarrays,catmove)
            catarrays = tiredcat
            #print("cat slept")
            cattiredness = 0

        #Are the cats thirsty?
        cattiredness = cattiredness + 5
        if cattiredness > 60:
            tiredcat = tmovement(catarrays,catmove)
            catarrays = tiredcat
            #print("cat slept")
            cattiredness = 0

        #Kitten behaviors:

        #Are the kittens tired?
        kittentiredness = kittentiredness + 2.5
        if kittentiredness > 60:
            tiredkitten= tmovement(kittenarrays,kittenmove)
            kittenarrays = tiredkitten
            #print("kitten slept")
            kittentiredness = 0
        #Are the kittens      
        #Mapping statements
        map_kitten(kittenarrays,'y')
        map_cat(catarrays,'r') 
       
        
        #fed every 3 hours:
        if x%3 == 0:
            map_feature(water, "c")
        if x%6 == 0:
            map_feature(food, "g")
        map_feature(bed, "b")
        map_feature(boxes, "m")
        map_feature(boundary, "k")
        
        plt.title("Simulating Cats :D(time is: " + str(x) + " hours)")
        plt.xlim(-1,MAXCOL)
        plt.ylim(-1,MAXROW)
        #plt.xticks(range(30))
        #plt.yticks(range(30))
        plt.pause(0.5)
        plt.clf()
        
if __name__ == "__main__":
    main()
