import re
import numpy as np
def first():
    with open('Day6/input.txt', 'r') as file:
        total=0
        times=[46689866]
        distances=[358105418071080]
        total=1
        for x in range(1):
            count=0        
            for i in range(int(times[x])):
                holdDown=i
                speed=holdDown
                dis=speed*(int(times[x])-i)
                if(dis>int(distances[x])):
                    count+=1 
            total*=count
            print(total)
            
           
           
            
       

            

first()