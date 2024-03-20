import re
import numpy as np
import sys
sys.setrecursionlimit(2000000)
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

def traverse(array, y, x, maxY, maxX, lastmove, startvalue=0):
    if x < 0 or x >= maxX or y < 0 or y >= maxY:
        print("you are outside of the map chill")
        return None  

    cur = array[y][x]
    print(f'you are currently at {y,x}')
    print(cur)

    if cur == 'S' and startvalue != 0:
        print("reached end of the line")
        print(f'and this took {startvalue} steps')
        return startvalue  # Path completed

    # Explore North
    if y > 0 and cur in('S','|','L','J') and array[y-1][x] in ('|', '7', 'F', 'S') and lastmove != 's':
        #print("north")
        north = traverse(array, y-1, x, maxY, maxX, 'n', startvalue+1)
        

    # Explore South
    if y < maxY - 1 and cur in('S','7','F','|') and  array[y+1][x] in ('|', 'J', 'L', 'S') and lastmove != 'n':
        print("south")
        south = traverse(array, y+1, x, maxY, maxX, 's', startvalue+1)

    # Explore East
    if x < maxX - 1 and cur in('S','-','F','L') and array[y][x+1] in ('-', 'J', '7', 'S') and lastmove != 'w':
        print("east")
        east = traverse(array, y, x+1, maxY, maxX, 'e', startvalue+1)
        
    # Explore West
    if x > 0 and cur in('S','-','J','7') and array[y][x-1] in ('-', 'F', 'L', 'S') and lastmove != 'e':
        print("west")
        west = traverse(array, y, x-1, maxY, maxX, 'w', startvalue+1)
        
    


def findS(array):
    for index,row in enumerate(array):
        for inner_index,cur in enumerate(row):
            if(cur=='S'):
                y=index
                x=inner_index
                return y,x
                


first()