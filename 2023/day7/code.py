import re

def day7(input):
    ans = 0
    cards = list("AKQJT98765432")
    #print(cards)
    strengthDict = {}
    for i in range(len(cards)):
        strengthDict[cards[i]] = 13 - i
    #print(strengthDict)
    bidDict = {}
    #RankDict = {'FiveKind':{}, 'FourKind':{}, 'FullHouse':{}, 'ThreeKind':{}, 'TwoPair':{}, 'OnePair':{}, 'HighCard':{}}
    valDict = {}
    valList = []

    #parse list
    lineList = list(open(input))
    for line in lineList:
        line = re.sub("\n", "", line)
        line = re.split("\s", line)
        deck = line[0]
        bid = int(line[1])
        bidDict[deck] = bid
        
        #compute strength
        deckVal = ""
        for i in range(len(deck)):
            strength = strengthDict[deck[i]]
            if strength < 10:
                deckVal += "0" + str(strength) + "00"
            else:
                deckVal += str(strength) + "00"
        
        
        #compute rank
        cardDict = {}
        for i in range(len(deck)):
            if deck[i] not in cardDict:
                cardDict[deck[i]] = 1
            else:
                cardDict[deck[i]] += 1
        kind = list(cardDict.values())
        kind.sort(reverse=True)
        kind = "".join([str(kind[i]) for i in range(len(kind))])
        #print(kind)
        if kind == "5":
            deckVal = int(deckVal) * 1000000000000
        elif kind == "41":
            #FourKind.append(deck)
            deckVal = int(deckVal) * 10000000000
        elif kind == "32":
            #FullHouse.append(deck)
            deckVal = int(deckVal) * 100000000
        elif kind == "311":
            #ThreeKind.append(deck)
            deckVal = int(deckVal) * 1000000
        elif kind == "221":
            #TwoPair.append(deck)
            deckVal = int(deckVal) * 10000
        elif kind == "2111":
            #OnePair.append(deck)
            deckVal = int(deckVal) * 100
        elif kind == "11111":
            #HighCard.append(deck)
            deckVal = int(deckVal) * 1
        print(deck, deckVal)

        valDict[deckVal] = deck
        valList.append(deckVal)

    rank = 1
    valList.sort()
    for v in valList:
        ans += bidDict[valDict[v]] * rank
        print(valDict[v], bidDict[valDict[v]], rank)
        rank += 1
        
    print(ans)

    #253304319
day7('input.txt')