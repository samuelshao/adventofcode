import re

def day5(input):
    lines = list(open(input))
    seeds = {}
    mapOrder = []
    mapRange = {}

    for line in lines:
        line = re.sub("\n", "", line)
        x = re.search(r"\bmap", line)
        
        if x:
            x = re.split("\s|-", x.string)
            sourceName, destinationName = x[0], x[2]
            mapRange[destinationName] = {}
            mapOrder.append(destinationName)
        elif len(line) > 0:
            line = re.split("\s", line)
            if line[0] == "seeds:":
                for i in range(1, len(line), 2):
                    seeds[int(line[i])] = int(line[i+1])
                #print(seeds)
            else:
                sourceID = int(line[1])
                destinationID = int(line[0])
                offset = int(line[2])
                sourceTuple = (sourceID, sourceID + offset - 1)
                destinationTuple = (destinationID, destinationID + offset - 1)
                mapRange[destinationName][sourceTuple] = destinationTuple

    minLocation = float('inf')
    for seed in seeds:
        for index in range(seeds[seed]):
            currID = seed + index
            #print(currID)
            for mapName in mapOrder:
                for item in mapRange[mapName]:
                    sourceStart = item[0]
                    sourceEnd = item[1]
                    destinationStart = mapRange[mapName][item][0]
                    destinationEnd = mapRange[mapName][item][1]
                    
                    if currID >= sourceStart and currID <= sourceEnd:
                        offset = destinationStart - sourceStart
                        currID += offset
                        break
                
            if currID < minLocation:
                minLocation = currID
        
    print(minLocation)

day5('input.txt')