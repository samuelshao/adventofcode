import re

def day8(input):
    lines = list(open(input))
    for line in lines:
        line = re.sub("\n", "", line)

    moves = re.sub("\n", "", lines[0])
    routes = {}
    for i in range(2, len(lines)):
        route = re.findall('[A-Z]{3}', lines[i])
        curr = route[0]
        left = route[1]
        right = route[2]
        routes[curr] = [left, right]
            
    source = "AAA"
    destination = "ZZZ"
    currLocation = source
    steps = 0

    while currLocation != destination:
        nextLocation = ""
        for move in moves:
            if move == "L":
                nextLocation = routes[currLocation][0]
                # print("moving left  from ", currLocation, " to ", nextLocation)
            else:
                nextLocation = routes[currLocation][1]
                # print("moving right from ", currLocation, " to ", nextLocation)
            currLocation = nextLocation
            steps += 1

    # print("move complete, steps taken: ", steps)
    print(steps)

day8('input.txt')