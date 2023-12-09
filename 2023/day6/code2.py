import re
import math

def day6(input):
    lines = list(open(input))
    timeList = []
    distList = []
    d = {}
    ansList = []
    
    for line in lines:
        line = re.sub("\n", "", line)

        t = re.search(r"\bTime:", line)
        d = re.search(r"\bDistance:", line)

        if t:
            t = re.split("\s", t.string)
            for i in range(1, len(t)):
                if len(t[i]) > 0:
                    timeList.append(t[i])

        if d:
            d = re.split("\s", d.string)
            for i in range(1, len(d)):
                if len(d[i]) > 0:
                    distList.append(d[i])
    maxTime = "".join(timeList)
    maxDist = "".join(distList)

    print(maxTime, maxDist)
    # x * (maxTime - x) = maxDist + 1
    # x * maxTime - x ** 2 - maxDist - 1 = 0
    # x = ?
    a = -1
    b = int(maxTime)
    c = -1 * (int(maxDist) + 1)
    print(a, b, c)

    x1 = (-1 * b + math.sqrt((b**2) - 4 * a * c)) // (2 * a)
    x2 = (-1 * b - math.sqrt((b**2) - 4 * a * c)) // (2 * a)
    print(int(x1), int(x2))
    print(int(x2) - int(x1))
day6('input.txt')