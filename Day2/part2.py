import re
def get_id(line):
    name_game=(line.split(":")[0])
    id=(name_game.split(" ")[-1])
    return id
main_dict={
    "red":12,
    "green": 13,
    "blue":14
}
#ok
def regex(colour, line):  
    pattern = rf'(\d+)\s*{colour}'
    matches = re.findall(pattern, line)
    max=0
    for match in matches:  
        if int(match) > max:
            max=int(match)
    return max

def all_regex(line):
    max_green=regex("green", line)
    max_red=regex("red", line)
    max_blue=regex("blue", line)    
    return max_green*max_red*max_blue  

def main():
    with open('Day2/input.txt', 'r') as file:  
        total=0     
        for line in file:  
            print("NEW BEGINNING")
            prod=all_regex(line)
            total+=prod
    print(total)
main()