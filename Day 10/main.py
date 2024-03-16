import re
import numpy as np
def first():

    
    with open('Day 10/input.txt', 'r') as file: 
        array=[]
        
        total=0
        for index,line in enumerate(file):
            
            line=line.strip()
            cur=[]
            for char in line:
                cur.append(char)
            array.append(cur)
        maxY=len(array)
        maxX=len(array[0])

        y,x=findS(array)


        cur=array[y][x]
        print(traverse(array,y,x,maxY,maxX,'y',0))
def verify(y,x,maxY,maxX):
    return not (x < 0 or x >= maxX or y < 0 or y >= maxY)
    
def traverse(array, y, x, maxY, maxX,lastmove,startvalue=0):    
   
    if x < 0 or x >= maxX or y < 0 or y >= maxY:
        return None
        print("outside of the map bro")

    
        
    
    cur = array[y][x]
    print(cur)

    if cur == 'S' and startvalue != 0:
        return startvalue

    if y > 0 and array[y-1][x] in ('|', '7', 'F') and lastmove != 's':  # North
        print("north")
        return traverse(array, y-1, x, maxY, maxX, 'n', startvalue+1)
    if y < maxY - 1 and array[y+1][x] in ('|', 'J', 'L') and lastmove != 'n':  # South
        print("south")
        return traverse(array, y+1, x, maxY, maxX, 's', startvalue+1)
    if x < maxX - 1 and array[y][x+1] in ('-', 'J', '7') and lastmove != 'w': # East
        print("east")
        return traverse(array, y, x+1, maxY, maxX, 'e', startvalue+1)
    if x > 0 and array[y][x-1] in ('-', 'F', 'L') and lastmove != 'e': # West
        print("west")
        return traverse(array, y, x-1, maxY, maxX, 'w', startvalue+1)
    return None


def findS(array):
    for index,row in enumerate(array):
        for inner_index,cur in enumerate(row):
            if(cur=='S'):
                y=index
                x=inner_index
                return y,x
                


first()