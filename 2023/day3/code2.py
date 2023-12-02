def day1(input):
    ans = 0
    f = open(input)
    intSet = set('1234567890')
    linelist = []
    gearDict = {}
    adjacents = []

    for line in f.read().split('\n'):
        linelist.append(line)

    num = ""
    for i in range(len(linelist)):
        for j in range(len(linelist[i])):
            if linelist[i][j] in intSet:
                num += linelist[i][j]

                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < len(linelist) and y >= 0 and y < len(linelist[i]):
                            if [x, y] not in adjacents:
                                adjacents.append([x, y])
            else:
                while adjacents:
                    coords = adjacents.pop()
                    symbol = linelist[coords[0]][coords[1]]
                    if symbol == '*':
                        key = str(coords[0]) + ' ' + str(coords[1])
                        if key not in gearDict:
                            gearDict[key] = [int(num)]
                        else:
                            gearDict[key].append(int(num))
                        adjacents = []
                num = ""
    print(gearDict)

    for key in gearDict:
        if len(gearDict[key]) == 2:
            prod = gearDict[key][0] * gearDict[key][1]
            ans += prod
    print(ans)
    return ans

day1('input.txt')