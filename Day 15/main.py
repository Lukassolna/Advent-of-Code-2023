import re
import numpy as np
def first():
    with open('Day 15/input.txt', 'r') as file:
        total=0
        for line in file:
            ok=line.split(",")
            
            for group in ok:
                cur=0
                for chara in group:
                    ye=ord(chara)
                    cur=(cur+ye)*17
                    cur=cur%256
                total+=cur
                    
    print(total)

          


def test():
    group="cm-"
    cur=0
    for chara in group:
                        ye=ord(chara)
                        cur=(cur+ye)*17
                        cur=cur%256
                        print(cur)
    print(cur)

first()