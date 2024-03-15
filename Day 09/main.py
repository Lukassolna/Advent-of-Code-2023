import re
import numpy as np
def first():

    map={}
    with open('Day 09/input.txt', 'r') as file: 
        total=0
        for index,line in enumerate(file):
            
            all=[]
            split=line.split(" ")
            intsplit=[int(x) for x in split]
            all.append(intsplit)
            next=genNext(intsplit)
            all.append(next)
            while(not allzeros(next)):
                next=genNext(next)
                all.append(next) 
            increase=0     
            rev=reverse_array(all)
            for i,array in enumerate(rev):
                if(i != 0 and i != len(all)-1):
                    #print(array)
                    increase=array[-1]
                    next_array=rev[i+1]
                    rev[i+1].append(rev[i+1][-1]+increase)
                    
                    #all[len(all)-1-i].append(increase)
                    

                    #print(increase)
              
            total+=(rev[-1][-1])
        print(total)      

def reverse_array(arr):
    return arr[::-1]

                
def genNext(array):
    diff_array=[]
    for i in range(len(array)):
        if(i not in [0]):
            diff_array.append(array[i]-array[i-1])
    return diff_array

                

def allzeros(array):
    return all(element == 0 for element in array)

first()