import re
import numpy as np
import sys

def first(): 
    with open('Day 13/input.txt', 'r') as file: 
        arrays =[]   
        array=[]  
        for line in file:             
            if line.strip() == '':    
                arrays.append(array)
                array=[] 
                continue
            
            line = line.strip()
            cur = []
            for char in line:
                cur.append(char)
            array.append(cur) 
        if array:
            arrays.append(array)              
        return arrays

def findMiddleColumns(ar):
    pairs=[]
    for i in range(len(ar[0])):
        if i>0:
            if np.array_equal(ar[:,i], ar[:,i-1]):
                pairs.append((i,i-1))
    return pairs
            
def findMiddleRows(ar):
    pairs=[]
    for i in range(len(ar)):
        if i>0:
            if np.array_equal(ar[i], ar[i-1]):
                pairs.append((i,i-1))
    return pairs

def two_pointer_col(x_col,y_col,ar): 
    x=x_col
    y=y_col
    while x>=0 and y<len(ar[0]):
        if not np.array_equal(ar[:,x], ar[:,y]):
            return 0,0
        x=x-1
        y=y+1
    return x_col,y_col

def two_pointer_row(x_col,y_col,ar):
    x=x_col
    y=y_col
    while x>=0 and y<len(ar):
        if not np.array_equal(ar[x], ar[y]):
            return 0,0
        x=x-1
        y=y+1
    return x_col,y_col

def doall():
    ars=first()
    total=0
    for individual_array in ars:
        ar=np.asarray(individual_array)
        pairs=findMiddleColumns(ar)    
        row_pairs=findMiddleRows(ar)
        
        for pair in pairs:
            x_col,y_col=pair
            x_col,y_col=two_pointer_col(y_col,x_col,ar)
            total+= (y_col)
            
        for pair in row_pairs:
            x_row,y_row=pair
            x_row,y_row=two_pointer_row(y_row,x_row,ar)
            total+= (y_row*100)
    return total
print(doall())
