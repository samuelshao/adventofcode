import re
import math

def day8(input):
    lines = list(open(input))
    for line in lines:
        line = re.sub("\n", "", line)

    moves = re.sub("\n", "", lines[0])
    routes = {}
    for i in range(2, len(lines)):
        route = re.findall('[A-Z|0-9]{3}', lines[i])
        curr = route[0]
        left = route[1]
        right = route[2]
        routes[curr] = [left, right]

    currs = {}
    pathList = []

    for route in routes:
        if route[2] == 'A':
            currs[route] = 0

    for key in currs:
        steps = 0
        currLocation = key
        while currLocation[2] != 'Z':
            for move in moves:
                if move == 'L':
                    currLocation = routes[currLocation][0]
                else:
                    currLocation = routes[currLocation][1]
                steps += 1
                if currLocation[2] == 'Z':
                    break
        currs[key] = steps
        pathList.append(steps)

    #print(currs)

    #lcm
    currLCM = pathList[0]
    for num in pathList[1:]:
        currLCM = math.lcm(currLCM, num)

    print(currLCM)
    
        

day8('input.txt')