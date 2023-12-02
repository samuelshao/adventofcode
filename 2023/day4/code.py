import re

def day4(input):
    ans = 0
    winDict = {}
    copyDict = {}

    linelist = list(open(input))
    
    for line in linelist:
        line = line.replace('\n', ' ')
        line = re.split(': |\| |\n', line)

        cardID = re.findall("\d", line[0])
        cardID = "".join(cardID)
        winningNum = line[1]
        currNum = line[2]

        winningNum = re.split("\s", winningNum)
        currNum = re.split("\s", currNum)
        # print(cardID, "|", winningNum, "|", currNum)

        wins = 0
        for num in currNum:
            if len(num) > 0:
                if num in winningNum:
                    wins += 1

        print(cardID, wins)
        winDict[cardID] = wins
        copyDict[cardID] = 1

    #print(winDict)
    print(copyDict)

    for key in winDict:
        wins = winDict[key]
        for i in range(1, wins+1):
            copyID = str(int(key) + i)
            if copyID in copyDict:
                copyDict[copyID] += 1 * copyDict[key]
                     
        #print(cardID, "|", " ".join(winningNum), "|", " ".join(currNum))
        #print(cardID)
    print(copyDict)
    for key in copyDict:
        ans += copyDict[key]
    print(ans)
    return ans


day4('input.txt')