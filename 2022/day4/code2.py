def isOverlap(List1: list[int], List2: list[int])-> bool:
    set1, set2 = set(), set()
    for i in range(List1[0], List1[1]+1):
        set1.add(i)

    for i in range(List2[0], List2[1]+1):
        set2.add(i)

    for s in set1:
        if s in set2:
            return True
        
    return False

def day4(input):
    f = open(input, 'r')
    lines = f.readlines()
    pairs = 0
    for line in lines:
        ranges = line.split(',')
        ranges[1] = ranges[1].split('\n')[0]
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')
        for i in range(2):
            range1[i] = int(range1[i])
            range2[i] = int(range2[i])
        print(range1, range2)
        if isOverlap(range1, range2):
            pairs += 1

    print(pairs)
    return pairs

day4('input.txt')
