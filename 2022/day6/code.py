def day6(input):
    f = open(input, 'r')
    line = f.readline()
    line = list(line)
    #print(line)
    i = 0
    packetSet = set()
    messageSet = set()
    while line[i] != '\n':
        if line[i] not in packetSet:
            packetSet.add(line[i])
            if len(packetSet) == 4:
                break
        else:
            packetSet = set()

        i += 1
    packetIndex = i+1
    while line[i] != '\n':
        if line[i] not in messageSet:
            messageSet.add(line[i])
            if len(messageSet) == 14:
                messageIndex = i+1
                break
        else:
            messageSet = set()

        i += 1
    charsProcessed = messageIndex
    print(charsProcessed)
        
day6('input.txt')

