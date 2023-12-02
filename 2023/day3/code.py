def day1(input):
    ans = 0
    f = open(input)
    intSet = set('1234567890')
    linelist = []
    nums = []
    adjacents = []

    for line in f.read().split('\n'):
        linelist.append(line)

    # for line in linelist:
    #     for c in line:
    #         if c not in intSet and c != '.':
    #             print(c)
    num = ""
    for i in range(len(linelist)):
        for j in range(len(linelist[i])):
            if linelist[i][j] in intSet:
                num += linelist[i][j]
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and y >= 0 and x < len(linelist) and y < len(linelist[i]):
                            print(x, len(linelist), y, len(linelist[i]))
                            if [x, y] not in adjacents:
                                adjacents.append([x, y])
            else:
                while adjacents:
                    coords = adjacents.pop()
                    symbol = linelist[coords[0]][coords[1]]
                    if symbol != '.' and symbol not in intSet:
                        print(num)
                        print(adjacents)
                        nums.append(int(num))
                        adjacents = []
                num = ""
    #check adjacents

    # i = [0, 0]
    # for x in range(i[0]-1, i[0]+2):
    #     for y in range(i[1]-1, i[1]+2):
    #         print([x, y])

    print(nums)
    ans = sum(nums)
    print(ans)
    return ans

day1('input.txt')