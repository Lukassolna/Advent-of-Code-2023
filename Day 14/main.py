import re
import numpy as np
import sys

def first(): 
    with open('Day 14/input.txt', 'r') as file: 
         
        array=[]  
        for line in file:             
        
            line = line.strip()
            cur = []
            for char in line:
                cur.append(char)
            array.append(cur) 
        return np.array(array)
    
array=first()
print(array)
swap = True  # Initilize it to swap to enter the loop
while swap:
    swap = False  # Base case that will stop the loop if no swap was done
    for y in range(len(array[0])):
        cur = array[:, y]
        for i in range(len(cur)-1):
            current = cur[i]
            next_element = cur[i+1]
            if current == '.' and next_element == 'O':
                cur[i], cur[i+1] = cur[i+1], cur[i]  
                swap = True  # set the flag to continue the loop
print(f'array after transformation :\n {array}')

            
total=0
for y in range(len(array[0])):
        cur = array[:, y]
        for i in range(len(cur)):
            current=(cur[i])
            if(current=='O'):
                total+=(len(cur)-i)   
print(total)

    







