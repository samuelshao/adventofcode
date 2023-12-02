import re

def day4(input):
    ans = 0

    linelist = list(open(input))
    
    for line in linelist:
        line = line.replace('\n', ' ')
        line = re.split(': |\| |\n', line)
        #print(line)
        #print(line)
        cardID = re.findall("\d", line[0])
        cardID = "".join(cardID)
        print(cardID)


        #cardID = line[0]
        winningNum = line[1]
        currNum = line[2]

        winningNum = re.split("\s", winningNum)
        currNum = re.split("\s", currNum)

        wins = 0
        for num in currNum:
            if len(num) > 0:
                if num in winningNum:
                    wins += 1
        #print(wins)
        if wins > 1:
            ans += 2 ** (wins-1)
        else:
            ans += wins
                     
        #print(cardID, "|", " ".join(winningNum), "|", " ".join(currNum))
        #print(cardID)

    print(ans)
    return ans


day4('input.txt')