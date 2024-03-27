import re
import numpy as np
import sys
import matplotlib.pyplot as plt

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
    

def count():      
            total=0
            for y in range(len(array[0])):
                    cur = array[:, y]
                    for i in range(len(cur)):
                        current=(cur[i])
                        if(current=='O'):
                            total+=(len(cur)-i)   
            return total


outputs = []
for x in range(1,100):
    array=first()
    
    for i in range(x):
        # NORTH
        swap = True  # Initilize it to swap to enter the loop
        while swap:
            swap = False  # Base case that will stop the loop if no swap was done
            for y in range(len(array[0])):
                cur = array[:, y]
                for i in range(len(cur)-1):
                    current = cur[i]
                    next_element = cur[i+1]
                    if current == '.' and next_element == 'O':
                        cur[i], cur[i+1] = cur[i+1], cur[i]  # swap 
                        swap = True  # set the flag to continue the loop
        #print(f'array after transformation NORTH :\n {array}')

        # WEST
        swap = True  # Initilize it to swap to enter the loop
        while swap:
            swap = False  # Base case that will stop the loop if no swap was done
            for y in range(len(array)):
                cur = array[y]
                for i in range(len(cur)-1):
                    current = cur[i]
                    next_element = cur[i+1]
                    if current == '.' and next_element == 'O':
                        cur[i], cur[i+1] = cur[i+1], cur[i]  # swap 
                        swap = True  # set the flag to continue the loop
        #print(f'array after transformation  WEST:\n {array}')



        # South
        swap = True  # Initialize it to swap to enter the loop
        while swap:
            swap = False  # Base case that will stop the loop if no swap was done
            for y in range(len(array[0])):  
                cur = array[:, y]  # Current column
                for i in range(len(cur)-2, -1, -1):  # Start from the second to last element, move upwards
                    current = cur[i]
                    next_element = cur[i+1]
                    if current == 'O' and next_element == '.':
                        cur[i], cur[i+1] = cur[i+1], cur[i]  # Swap
                        swap = True  # Set the flag to continue the loop
        #print(f'array after transformation SOUTH :\n {array}')

        # EAST
        swap = True  # Initilize it to swap to enter the loop
        while swap:
            swap = False  # Base case that will stop the loop if no swap was done
            for y in range(len(array)):
                cur = array[y]
                for i in range(len(cur)-2, -1, -1): 
                    current = cur[i]
                    next_element = cur[i+1]
                    if current == 'O' and next_element == '.':
                        cur[i], cur[i+1] = cur[i+1], cur[i]  # swap 
                        swap = True  # set the flag to continue the loop
        #print(f'array after transformation EAST :\n {array}')



        

    outputs.append(count())

print(outputs)
plt.plot(range(1,100), outputs)
plt.xlabel('x')
plt.ylabel('Output')
plt.title('Function Output for x from 1 to 100')
plt.grid(True)
plt.show()