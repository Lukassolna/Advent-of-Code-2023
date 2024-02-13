def first():
    with open('Day1/input.txt', 'r') as file:
        total=0
        for line in file:
            line = line.strip()
            intList=[x for x in line if x.isdigit()]
            total+=int((f'{intList[0]}{intList[-1]}'))
    print(total)
