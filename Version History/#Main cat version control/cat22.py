# Author : Navin Samarakoon
# ID : 20471246
#
#catfinal(22).py - Simulating the behavior of cats 
#
# Revisions: 22nd version
#
#
#Comment index:
#0 - Dependencies
#1 - Base setups
#2 - Movement
#3 - Mapping
#4 - Defining variables
#5 - Initializing simulation
#6 - Print statements
#7 - Defining behaviors
#8 - Cat attributes (Catributes :D)
#9 - Kitten attributes
#10 - Plotting 



#0.1 - imports
from cat import Cat 
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox



#1.1 - Grid
MAXROW = 30
MAXCOL = 30

#1.2 - Setting up variables
STEPS = int(input("How many hours should we run the simulation for? "))
if STEPS = 0:
    print("must be a valid number")
if STEPS < 0:
    print("you dont have a time machine")

CATNO = int(input("How many cats to simulate? "))
if CATNO > 5:
    print("Too many cats :(")
    CATNO = int(input("try again: "))
if CATNO < 0:
    print("Do not kill the poor cats :(")
    CATNO = int(input("try again: "))

KITTENNO = int(input("How many kittens to simulate? "))
if KITTENNO > 5:
    print("Too many kittens :(")
    KITTENNO = int(input("try again: "))
if KITTENNO > 0:
    print("Do not kill the poor kittens :(")
    CATNO = int(input("try again: "))

#1.3 - Reading file
def readlists(filelist):
    externallist = [(int(l.split(",")[0]),int(l.split(",")[1])) for l in filelist[1:]]
    return externallist

#1.4 - Creating food and water sources
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

#1.5 - Boundary control
def boundaries(KITTENNO, boundarylist):
    for r in range(MAXROW):
        for c in range(MAXCOL):
            if (r, c) in boundarylist:
                for g in range(KITTENNO[r,c]):
                    KITTENNO[r,c] = KITTENNO[0,0]



#2.1 - Movement - base
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

#2.2 - Movement:happiness
def hmovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 14
                cmoved = 16
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#2.3 - Movement:tired
def tmovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 4 
                cmoved = 29
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#2.4 - Movement:hunger
def hunmovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 1
                cmoved = 2 
                nextgrid[rmoved,cmoved] += 1

    return nextgrid

#2.5 - Movement:thirst
def thimovement(current,moves):
    nextgrid = np.zeros((MAXROW,MAXCOL), dtype=int)
    for r in range(MAXROW):
        for c in range(MAXCOL):
            for i in range(current[r,c]):
                rmoved = 29
                cmoved = 1
                nextgrid[rmoved,cmoved] += 1

    return nextgrid



#3.1 - Mapping:boundaries
def map_boundary(thing,colour):
    xlist = []
    ylist = []
    slist = [20]
    for row,col in thing:
        ylist.append(MAXROW - row - 1)
        xlist.append(col)
    plt.scatter(xlist,ylist,s=slist,color=colour,marker='s')

#3.2 - Mapping:
def map_feature(thing,colour):
    xlist = []
    ylist = []
    for row,col in thing:
        ylist.append(MAXROW - row - 1)
        xlist.append(col)
    plt.scatter(xlist,ylist,color=colour,marker='s')

#3.3 - Finding image and zooming for kitten
def getImage1(path):
    return OffsetImage(plt.imread(path, format="png"), zoom=0.15)

#3.4 - Finding image and zooming for cat
def getImage2(path):
    return OffsetImage(plt.imread(path, format="png"), zoom=0.05)

#3.5 - Mapping the cat
def map_kitten(KITTENNO,colour):
    
    paths = ['cat3.png','cat3.png','cat3.png','cat3.png','cat3.png']
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

#3.6 - Mapping the kitten
def map_cat(CATNO,colour):
    
    paths = ['cat2.png','cat2.png','cat2.png','cat2.png','cat2.png']
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
    
    #4.1 - Happiness
    cathappy = 100
    kittenhappy = 100
    
    #4.2 - Tiredness
    cattiredness = 0
    kittentiredness = 0
    
    #4.3 - Hunger
    cathungry = 0
    kittenhungry = 0

    #4.4 - Thirst
    catthirst = 0
    kittenthirst = 0

    #4.5 - Moving amount
    catmove = [-4,0,1]
    kittenmove = [-5,0,1]
    
    #4.6 - Basic arrays
    nextgrid = np.zeros((MAXROW, MAXCOL), dtype=int)
    catarrays = np.zeros((MAXROW, MAXCOL), dtype=int)
    kittenarrays = np.zeros((MAXROW, MAXCOL), dtype=int)
    water, food, bed, boxes, boundary = sources("terrain.txt")
    
    print("/nSimulating Cats/n")



    #5 - Initializing the simulation

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
        
        #6.1 - Base:
        print('\n')
        print("TIME:", x, "hours")
        print('\n')
        
        #6.2 - Cat info:
        if CATNO > 0:
            print("Cat info:")
            print("How Happy are the cats: ", cathappy, "/ 100")
            print("How Tired are the cats: ", cattiredness, "/ 100")
            print("How Hungry are the cats: ", cathungry,"/ 100")
            print("How Thirsty are the cats: ", catthirst,"/ 100")
            print('\n')
        
        #6.3 - Kitten info:
        if KITTENNO > 0:
            print("Kitten info:")
            print("How Happy are the kittens: ", kittenhappy, "/ 100")
            print("How Tired are the kittens: ", kittentiredness,"/ 100")
            print("How Hungry are the kittens: ", kittenhungry,"/ 100")
            print("How Thirsty are the kittens: ", kittenthirst,"/ 100")
            print('\n')



        #7.1 - Normal cat behavior
        catnext = movement(catarrays,catmove)
        kittennext = movement(kittenarrays,kittenmove)

        #7.2 - Normal kitten behavior
        catarrays = catnext
        kittenarrays = kittennext

        #7.3 - Boundary behaviors
        boundaries(kittennext, boundary)



        #8 - Cat behaviors:

        #8.1 - Are the cats happy?
        cathappy = cathappy - 10
        if cathappy < 20:
            happycat = hmovement(catarrays,catmove)
            catarrays = happycat
            print("cats played in box")
            cathappy = 100
        
        #8.2 - Are the cats tired?
        cattiredness = cattiredness + 5
        if cattiredness > 60:
            tiredcat = tmovement(catarrays,catmove)
            catarrays = tiredcat
            print("cats slept")
            cattiredness = 0
        
        #8.3 - Are the cats hungry?
        cathungry = cathungry + 2.5
        if x%6 == 0 and cathungry > 80:
            hungrycat = hunmovement(catarrays,catmove)
            catarrays = hungrycat
            print("cats ate")
            cathungry = 0

        #8.4 - Are the cats thirsty?  
        catthirst = catthirst + 5
        if x%3 == 0 and catthirst > 40:
            thirstcat = thimovement(catarrays,catmove)
            catarrays = thirstcat
            print("cats drank")
            catthirst = 0



        #9 - Kitten behaviors:

        #9.1 - Are the kittens happy?
        kittenhappy = kittenhappy - 5 
        if kittenhappy < 40:
            happykitten= hmovement(kittenarrays,kittenmove)
            kittenarrays = happykitten
            print("kitten played in box")
            kittenhappy = 100
        
        #9.2 - Are the kittens tired?
        kittentiredness = kittentiredness + 2.5
        if kittentiredness > 60:
            tiredkitten= tmovement(kittenarrays,kittenmove)
            kittenarrays = tiredkitten
            print("kitten slept")
            kittentiredness = 0
        
        #9.3 - Are the kittens hungry?
        kittenhungry = kittenhungry + 5
        if x%6 == 0 and kittenhungry > 50:
            hungrykitten= hunmovement(kittenarrays,kittenmove)
            kittenarrays = hungrykitten
            print("kitten ate")
            kittenhungry = 0
        
        #9.4 - Are the kittens thirsty?
        kittenthirst = kittenthirst + 2.5
        if x%3 == 0 and kittenthirst > 30:
            thirstkitten= thimovement(kittenarrays,kittenmove)
            kittenarrays = thirstkitten
            print("kitten drank")
            kittenthirst = 0        



        #10 - Mapping
        map_kitten(kittenarrays,'y')
        map_cat(catarrays,'r') 
       
        
        #10.1 - Replenishable food and water
        if x%6 == 0:
            map_feature(food, "g")
        if x%3 == 0:
            map_feature(water, "b")
        map_feature(bed, "c")
        map_feature(boxes, "m")
        map_boundary(boundary, "k")
        
        #10.2 Final plots
        plt.title("Simulating Cats :D(time is: " + str(x) + " hours)")
        plt.xlim(-1,MAXCOL)
        plt.ylim(-1,MAXROW)
        #plt.xticks(range(30))
        #plt.yticks(range(30))
        plt.pause(0.5)
        plt.clf()

if __name__ == "__main__":
    main()
