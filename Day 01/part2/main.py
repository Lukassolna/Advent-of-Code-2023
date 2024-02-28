dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def do():
    total=0
    with open('Day1/part2/small_input.txt', 'r') as file:       
        for line in file:
            total+=int(f'{first(line)}{last(line)}')

            print(f'{first(line)}')
        return total                             
    
def first(line):
        so_far=""
        for letter in line:
            if letter.isdigit():
                first_int=int(letter)
                return first_int          
            so_far+=letter
            for num in list:
                if num in so_far:      
                    first_int=((dict.get(num)))
                    return first_int

def last(line):
    reversed=line[::-1]
    so_far=''
    for letter in reversed:
        if letter.isdigit():
           return letter
        so_far+=letter
        for num in list:
            if num in so_far[::-1]:      
                int=(str(dict.get(num)))
                return int
print(do())

       
            




