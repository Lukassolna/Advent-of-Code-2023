import re
import numpy as np
def first():
    with open('Day6/input.txt', 'r') as file:
        total=0
        times=[]
        distances=[]
        for index,line in enumerate(file,start=1):
            line = line.strip()
            parts=line.split()
            if(index==1):
                for i in range(1,5):
                    times.append(parts[i])
                
            if(index==2):
                for i in range(1,5):
                    distances.append(parts[i])
        print(times)

        total=1
        for x in range(4):
            count=0
           
            for i in range(int(times[x])):
                holdDown=i
                speed=holdDown
                dis=speed*(int(times[x])-i)
                if(dis>int(distances[x])):
                    count+=1 
            total*=count
            print(total)
            
            # Now you have the times and distances as lists of integers
           
            
       

            

first()