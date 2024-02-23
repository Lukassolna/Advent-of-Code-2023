import re
import numpy as np



def first():
    total=[]
    copies=[]
    with open('Day4/input.txt', 'r') as file:
        
        for index,line in enumerate(file,start=1):
            print("currently processing line", index)
            line = line.strip()
            parts=line.split(" | ")
            cleaned_rows = re.sub(r'^.*?:\s*', '', parts[0])
            first_nums=cleaned_rows.split(" ")
            second_nums = re.split(r'\s+', parts[1])
            first_nums=[x for x in first_nums if x not in '']
            second_nums=[x for x in second_nums if x not in '']
            matching= [x for x in second_nums if x in first_nums]
            
            match_count=len(matching)
            #process the copies
            
            count=copies.count(index)
            for i in range(count):
                total.append(index)
            
            #print(f"counting occurnces of {index}: ", count)
            for y in range(count):
                for i in range(1,(match_count+1)):
                    cur=i+index                
                    copies.append(cur)

            # processs the original
            for i in range(1,(match_count+1)):
                cur=i+index                
                copies.append(cur)


            #print(copies)
            total.append(index)
        mang=0    
        for i in range(212):
            mang+=total.count(i)
        print(mang)
        print(np.sort(total))

            

first()