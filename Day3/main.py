import pandas as pd

# 2d array to hold all our numbers
array = []
all_valid=[]

with open('Day3/input.txt', 'r') as file:
    for line in file:
        
        current_line = []
        for letter in line.strip():  
            current_line.append(letter)  
        array.append(current_line)  

def find_grouped_numbers_in_array(array):
    numbers = []  # List to store found numbers
    for row in array:
        current_number = ''  # String to build the current number
        for char in row:
            if char.isdigit():  
                current_number += char
            else:
                if current_number:  
                    numbers.append(current_number)
                    current_number = ''  # Reset current number for the next group
        if current_number:  
            numbers.append(current_number)
    return numbers




            
def get_all_numbers():
    for i in range (len(array)):
        for y in range (len(array[0])):
            cur=array[i][y]
            if cur.isnumeric():
                print(f'Current number is : {cur}')
            
def is_symbol(sym):
    if sym.isnumeric():
        return False
    if sym=='.':
        return False
    else:
        return True

def next_to_symbol(x_pos, y_pos, array):
    max_x = len(array) - 1
    max_y = len(array[0]) - 1
    checks = [
        (x_pos + 1, y_pos),
        (x_pos - 1, y_pos),
        (x_pos, y_pos + 1),
        (x_pos, y_pos - 1),
        (x_pos + 1, y_pos + 1),
        (x_pos - 1, y_pos - 1),
        (x_pos - 1, y_pos + 1),
        (x_pos + 1, y_pos - 1)
    ]
    for x, y in checks:
        if 0 <= x <= max_x and 0 <= y <= max_y:
            if is_symbol(array[x][y]):
                return True
    return False

def loop_array(num, array, processed):
    for i in range(len(array)):
        for y in range(len(array[0])):
            cur = array[i][y]
            if cur == num and (i, y) not in processed:
                processed.add((i, y)) 
                return i, y
    return None, None  

def test():  
    final_list=[]
    processed = set()          
    grouped_numbers = find_grouped_numbers_in_array(array)
    for number in grouped_numbers:
        
        verify_num(number,processed)
                
def verify_num(number,processed):
    cur_cond=[]
    for num in number:
            x, y = loop_array(num, array, processed) 
            if x is not None and y is not None:  
                #print("Is found at the coordinates", x, y)
                next_to = next_to_symbol(x, y, array)
                cur_cond.append(next_to)
                
    if True in cur_cond:
       all_valid.append(int(number))
    else:
        print("")

            
test() 

print(sum(all_valid))     



    