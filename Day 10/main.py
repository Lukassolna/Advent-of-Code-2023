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

def traverse(array, y, x, maxY, maxX,lastmove,startvalue=0):
    # check 
    if x < 0 or x >= maxX or y < 0 or y >= maxY:
        print("outside of the map bro")
        return None
       
        
    cur = array[y][x]
    print(cur)
    if cur == 'S' and startvalue >0: 
        return startvalue
    # Example conditions for moving in different directions
    if array[y-1][x] in ('|', '7', 'F') and lastmove not in ['s']:  # North
        return traverse(array, y-1, x, maxY, maxX,'n',startvalue+1)
    elif array[y+1][x] in ('|', 'J', 'L')and lastmove not in ['n']:  # South
        return traverse(array, y+1, x, maxY, maxX,'s',startvalue+1)
    elif array[y][x+1] in ('-', 'J', '7')and lastmove not in ['w']: # East
        return traverse(array, y, x+1, maxY, maxX,'e',startvalue+1)
    elif array[y][x-1] in ('-', 'F', 'L')and lastmove not in ['e']: # West
        return traverse(array, y, x-1, maxY, maxX,'w',startvalue+1)
      


def findS(array):
    for index,row in enumerate(array):
        for inner_index,cur in enumerate(row):
            if(cur=='S'):
                y=index
                x=inner_index
                return y,x
                


first()