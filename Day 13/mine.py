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
                #print("empty")
                continue
            
            #print("first")
            line = line.strip()
            cur = []
            for char in line:
                cur.append(char)
            array.append(cur) 
        if array:
            arrays.append(array)              
        return arrays

def findMiddleColumns(ar):
    for i in range(len(ar[0])):
        #print(i)
        if i>0:
            #print(i)
            if np.array_equal(ar[:,i], ar[:,i-1]):
                print("found a matchging column")
                print(i,i-1)
                #print((ar[:,i], ar[:,i-1]))
                return i,i-1
    return 0,0
def findMiddleRows(ar):
    for i in range(len(ar)):
        if i>0:
            #print(i)
            if np.array_equal(ar[i], ar[i-1]):
                print("found a matching row")
                #print((ar[:,i], ar[:,i-1]))
                return i,i-1
    return 0,0
def two_pointer_col(x_col,y_col,ar): 
    x=x_col
    y=y_col
    while x>0 and y<len(ar[0]):
        #print(x,y)
        if np.array_equal(ar[:,x], ar[:,y]):
            x=x-1
            y=y+1
        else:
            return 0,0
    return x_col,y_col
def two_pointer_row(x_col,y_col,ar):
    x=x_col
    y=y_col
    while x>=0 and y<len(ar):
        if np.array_equal(ar[x], ar[y]):
            x=x-1
            y=y+1
        else:
            return 0,0
    return x_col,y_col
def doall():
    ars=first()
    #print(len(ars))
    total=0
    for arm in ars:
        ar=np.asarray(arm)
        #print("columns")
        #print(ar)
        x_col,y_col=findMiddleColumns(ar)
        #print(x_col,y_col)
        x_col,y_col=two_pointer_col(y_col,x_col,ar)
        #print(x_col,y_col)
        #print("rows")
        x_row,y_row=findMiddleRows(ar)
        #print(x_row,y_row)
        x_row,y_row=two_pointer_row(y_row,x_row,ar)
        #print(x_row,y_row)
        total+= ((y_row*100+y_col))
        print(total)
    return total
    
(doall())

#x_row,y_row=findMiddleRows(ar)
#print(x_row,y_row)






    