import re
import numpy as np
def first():

    map={}
    with open('Day 08/input.txt', 'r') as file:
        total=0
        path=''
        for index,line in enumerate(file):
            if(index==0 or index==1):
                path+=line
            if(index>1):
                line=line.strip()
                split=(line.split(' = '))
                first=split[0]
                second=split[1]
                second=second.replace('(','')
                second=second.replace(')','')
                split_second=second.split(",")
                left=split_second[0]
                right=split_second[1]
                first=first.strip()
                left=left.strip()
                right=right.strip()
                map[first] = (left,right)
                

        path=path.strip()
        next='AAA'
        count=0
    for i in range(10):
        path=path+path
    for letter in path:
        count+=1
        if(letter=="L"):
            next=map[next][0]
            print(next)
        if(letter=="R"):
            next=map[next][1]
            print(next)
        if(next=='ZZZ'):
            print(count)
            break


        
first()