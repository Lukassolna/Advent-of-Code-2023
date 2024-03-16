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
        y,x=findS(array)
        print(y,x)


def findS(array):
    for index,row in enumerate(array):
        for inner_index,cur in enumerate(row):
            if(cur=='S'):
                y=index
                x=inner_index
                return y,x
                


first()