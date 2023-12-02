def day1(input):
    f = open(input, 'r')
    lines = f.readlines()
    calories = []
    calorie = 0
    
    for line in lines:
        if line != "\n":
            line = list(line)
            line.pop()
            line = int("".join(line))
            calorie += line
        else:
            calories.append(calorie)
            calorie = 0

    print(max(calories))
    return max(calories)
        
day1('input.txt')
