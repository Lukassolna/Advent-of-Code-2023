import re
import numpy as np
def first():
    with open('Day4/input.txt', 'r') as file:
        total=0
        for index,line in enumerate(file,start=1):
            
            line = line.strip()
            parts=line.split(" | ")
            cleaned_rows = re.sub(r'^.*?:\s*', '', parts[0])
            first_nums=cleaned_rows.split(" ")
            second_nums = re.split(r'\s+', parts[1])
            first_nums=[x for x in first_nums if x not in '']
            second_nums=[x for x in second_nums if x not in '']
            matching= [x for x in second_nums if x in first_nums]
            inner_total=1

            for i in range(1,len(matching)):
                inner_total*=2
            if(len(matching)==0):
                inner_total=0
            total+=inner_total
            
        print(total)

            

first()