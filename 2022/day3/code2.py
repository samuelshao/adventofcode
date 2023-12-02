def priority(c: str) -> int:
    if 'a' <= c <= 'z':
        return ord(c) - 96
    elif 'A' <= c <= 'Z':
        return ord(c) - 38
    
def day3(input):
    f = open(input, 'r')
    lines = f.readlines()
    n = len(lines)
    ans = 0
    badges = []
    
    for i in range(0, n, 3):
        set1 = set(lines[i])
        set2 = set(lines[i+1])
        set3 = set(lines[i+2])

        for s in set1:
            if s != '\n' and s in set2 and s in set3:
                badges.append(s)
    print(badges)
    for badge in badges:
        ans += priority(badge)
    print(ans)
    return ans

day3('input.txt')
