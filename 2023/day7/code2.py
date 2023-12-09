import re

def day7(input):
    ans = 0
    cards = list("AKQT98765432J")
    strengthDict = {}
    for i in range(len(cards)):
        strengthDict[cards[i]] = 13 - i
    bidDict = {}
    RankDict = {'HighCard':{}, 'OnePair':{}, 'TwoPair':{}, 'ThreeKind':{}, 'FullHouse':{}, 'FourKind':{}, 'FiveKind':{}}
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
        jCount = 0
        for i in range(len(deck)):
            strength = strengthDict[deck[i]]
            if deck[i] == 'J':
                jCount += 1
            if int(strength) < 10:
                deckVal += '0' + str(strength) + '0'
            else:
                deckVal += str(strength) + '0'
        
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

        if kind == "5":
            RankDict['FiveKind'][deck] = deckVal
        elif kind == "41":
            #FourKind.append(deck)
            if jCount == 1 or jCount == 4:
                RankDict['FiveKind'][deck] = deckVal
            else:
                RankDict['FourKind'][deck] = deckVal
        elif kind == "32":
            #FullHouse.append(deck)
            if jCount == 1:
                RankDict['FourKind'][deck] = deckVal
            elif jCount == 2 or jCount == 3:
                RankDict['FiveKind'][deck] = deckVal
            else:
                RankDict['FullHouse'][deck] = deckVal
        elif kind == "311":
            #ThreeKind.append(deck)
            if jCount == 1 or jCount == 3:
                RankDict['FourKind'][deck] = deckVal
            else:
                RankDict['ThreeKind'][deck] = deckVal
        elif kind == "221":
            #TwoPair.append(deck)
            if jCount == 1:
                RankDict['FullHouse'][deck] = deckVal
            elif jCount == 2:
                RankDict['FourKind'][deck] = deckVal
            else:
                RankDict['TwoPair'][deck] = deckVal
        elif kind == "2111":
            #OnePair.append(deck)
            if jCount == 1 or jCount == 2:
                RankDict['ThreeKind'][deck] = deckVal
            else:
                RankDict['OnePair'][deck] = deckVal
        elif kind == "11111":
            #HighCard.append(deck)
            if jCount == 1:
                RankDict['OnePair'][deck] = deckVal
            else:
                RankDict['HighCard'][deck] = deckVal

    #print(RankDict)

    # d = dict(sorted(d.items(), key=lambda item:item[1]))
    for key in RankDict:
        RankDict[key] = dict(sorted(RankDict[key].items(), key=lambda item: item[1]))

    rank = 1
    for key in RankDict:
        for key2 in RankDict[key]:
            #print(key2, key, RankDict[key][key2], rank)
            cardVal = bidDict[key2] * rank
            #print(bidDict[key2], '*', rank, '=', cardVal)
            ans += cardVal
            rank += 1

    print(ans)

    #253362743

day7('input.txt')
