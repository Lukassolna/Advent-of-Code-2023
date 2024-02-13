def first():
    with open('Day1/input.txt', 'r') as file:
        total=0
        for line in file:
            line = line.strip()
            intList=[x for x in line if x.isdigit()]
            total+=int((f'{intList[0]}{intList[-1]}'))
    print(total)

def second():
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


