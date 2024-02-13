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
def regex(colour, line):  
    pattern = rf'(\d+)\s*{colour}'
    matches = re.findall(pattern, line)
    for match in matches:  
        if int(match) > main_dict.get(colour): 
            return True
    return False

def all_regex(line):
    if regex("green", line) or regex("red", line) or regex("blue", line):
        return False
    return get_id(line)  

def main():
    with open('Day2/input.txt', 'r') as file:  
        total=0     
        for line in file:
            print("NEW BEGINNING")
            id=all_regex(line)
            total+=int(id)
            print(total)
        

main()
