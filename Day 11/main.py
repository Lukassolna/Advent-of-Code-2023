import re
import numpy as np
import sys

def first(runs): 
    with open('Day 11/input.txt', 'r') as file: 
        array = []    
        for line in file:
            #print("first")
            line = line.strip()
            cur = []
            for char in line:
                cur.append(char)
            array.append(cur)
            if '#' not in line:
                #print("empty space 1")
                new_cur = []
                for char in line:
                    new_cur.append(char)
                # Make a copy to optimize performance
                array.extend([new_cur.copy() for _ in range(runs-1)])
        return array 



def second(input,runs):
    new = []

    for row in input:
        #print("second")
        new_row = []
        for i in range(len(row)):
            new_row.append(row[i])
            
            if '#' not in [input[r][i] for r in range(len(input))]:
               # print("empty space 2 ")
                
                new_row.extend([row[i]] * (runs - 1))
        
        new.append(new_row)
    
    return new
xes=[]
yes=[]
def doall(runs):
    array=first(runs)
    new=second(array,runs)

    pos_list=[]
    for outer,line in enumerate(new):
        for inner,pos in enumerate(line):
            if pos=='#':
                
                pos_list.append((outer,inner))
                
    #print(pos_list)
    total=0
    for index,positions in enumerate(pos_list):
        x,y=positions
        for i in range(index+1,len(pos_list)):
            compx,compy=(pos_list[i])
            distance=abs(x-compx)+abs(y-compy)
            total+=distance
        if(index==len(pos_list)-1):
            print(f" this iteration was finished and total is {total}")
            return runs,total
        
    
for i in range(1,30):
    x,y=doall(i)
    xes.append(x)
    yes.append(y)

np_x=np.array(xes)
np_y=np.array(yes)

print(x)

slope, intercept = np.polyfit(np_x, np_y, 1) # linear fit 
print(f"Slope: {slope}, Intercept: {intercept}")

predicted_y = slope * 1000000 + intercept
print(predicted_y)
    