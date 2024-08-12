import re
import numpy as np
import sys
def parse_input():
    with open('Day 16/input.txt', 'r') as file:
        
        grid = []
        for line in file:
           grid.append(line)  
        return grid




def move():
    if dir=='right':
        y,x=y,x+1
    if dir=='left':
        y,x=y,x-1
    if dir=='up':
        y,x=y-1,x
    if dir=='down':
        y,x=y+1,x

full=parse_input()
y,x=0,0
dir='right'
first_char=full[y][x]
print(first_char)


move()
cur_char=full[y][x]

if cur_char=='.':
    dir=dir

## mirror
if cur_char=='/':
    if dir=='right':
        dir='up'
     
    if dir=='left':
        dir='down'
     
    if dir=='up':
        dir='right'
      
    if dir=='down':
        dir='left'

     
if cur_char=='\'':
    if dir=='right':
        dir='down'
     
    if dir=='left':
        dir='up'
     
    if dir=='up':
        dir='left'
      
    if dir=='down':
        dir='right'




if cur_char=='|':
    split()
    #split
if cur_char=='-':
    split()
    #split
