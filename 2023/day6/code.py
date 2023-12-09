import re

def day6(input):
    lines = list(open(input))
    timeList = []
    distList = []
    d = {}
    ansProd = 0
    
    for line in lines:
        line = re.sub("\n", "", line)

        t = re.search(r"\bTime:", line)
        d = re.search(r"\bDistance:", line)

        if t:
            t = re.split("\s", t.string)
            for i in range(1, len(t)):
                if len(t[i]) > 0:
                    timeList.append(int(t[i]))

        if d:
            d = re.split("\s", d.string)
            for i in range(1, len(d)):
                if len(d[i]) > 0:
                    distList.append(int(d[i]))

    for i in range(len(timeList)):
        maxTime = timeList[i]
        maxDist = distList[i]

        x = 0
        ans = 0
        for x in range(1, maxTime+1):
            #currDist = x * (maxTime - x)
            currDist = (x * maxTime) - (x ** 2)
            if currDist > maxDist:
                ans += 1
        
        if ansProd <= 0:
            ansProd = ans
        else:
            ansProd *= ans
        
    print(ansProd)

day6('input.txt')