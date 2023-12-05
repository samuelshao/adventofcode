import re

def day5(input):
    lines = list(open(input))
    seeds = []

    currMap = ""
    
    mapping = {}


    for line in lines:
        line = re.sub("\n", "", line)
        #print(line)
        x = re.search(r"\bmap", line)
        if x:
            x = re.split("\s|-", x.string)
            sourceName = x[0]
            destinationName = x[2]
            #print(sourceName, "to", destinationName)
            currMap = destinationName
            mapping[currMap] = {}
        elif len(line) > 0:
            line = re.split("\s", line)
            
            if line[0] == "seeds:":
                for i in range(1, len(line)):
                    seeds.append(int(line[i]))
                print(seeds)
            else:
                #print(line)
                sourceID = int(line[1])
                destinationID = int(line[0])
                offset = int(line[2])
                sourceTuple = (sourceID, sourceID+offset-1)
                destinationTuple = (destinationID, destinationID+offset-1)
                mapping[currMap][sourceTuple] = destinationTuple

    print(mapping)
    locations = []
    for seed in seeds:
        currNum = seed
        for key in mapping:
            print(key)
            for item in mapping[key]:
                print(item, mapping[key][item])
                if currNum >= item[0] and currNum <= item[1]:
                    diff = mapping[key][item][0] - item[1]
                    currNum += diff
                    break
            
        locations.append(currNum)

    print(locations)

day5('testinput.txt')