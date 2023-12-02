def day5(input):
    #file ops
    f = open(input, 'r')
    lines = f.readlines()

    #variable declarations
    crates = []
    movesIndex = 0
    cratesIndex = 0
    stackIndex = {}
    moves = []

    #obtain the crates in a matrix
    for i in range(len(lines)):
        if lines[i] == '\n':
            cratesIndex = i-1
            movesIndex = i+1
            break
        line = list(lines[i])
        line.pop()
        crates.append("".join(line))

    #find the index of each stack
    stacks = crates[-1]
    for i in range(len(stacks)):
        if stacks[i].isalnum():
            stackIndex[int(stacks[i])] = i
    stacks = []
    for key in stackIndex:
        stack = []
        for i in range(cratesIndex):
            if crates[i][stackIndex[key]] != ' ':
                stack.append(crates[i][stackIndex[key]])
        stack.reverse()
        stacks.append(stack)

    #obtain the move instructions
    for i in range(movesIndex, len(lines)):
        s = lines[i].split(' ')
        temp = list(s[5])
        temp.pop()
        temp = "".join(temp)
        moves.append([int(s[1]), int(s[3]), int(temp)])
    #print(moves)

    #perform the moves on stacks
    for move in moves:
        m = move[0]
        f = move[1]
        t = move[2]
        c = stacks[f-1][-m:]
        stacks[f-1] = stacks[f-1][:-m]
        stacks[t-1] += c

    print(stacks)
    ans = []
    for stack in stacks:
        ans.append(stack[-1])
    print("".join(ans))
    return ans

day5('input.txt')
