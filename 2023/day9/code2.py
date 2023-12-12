import re

def day9(input):
    lines = list(open(input))
    ans = 0

    for line in lines:
        line = re.sub("\n", "", line)
        line = re.split("\s", line)
        hist = []
        diffs = []
        for val in line:
            diffs.append(int(val))
        currSum = sum(diffs)
        hist.append(diffs)
        
        while currSum != 0:
            #print(diffs)
            newDiffs = []
            for i in range(1, len(diffs)):
                newDiffs.append(diffs[i] - diffs[i-1])
            hist.append(newDiffs)
            diffs = newDiffs
            currSum = sum(diffs)
        #print(hist)
        n = len(hist)
        pred = 0
        for i in range(n-1, -1, -1):
            pred = hist[i][0] - pred
        #print(pred)
        print(pred)
        ans += pred

    print(ans)

day9('input.txt')