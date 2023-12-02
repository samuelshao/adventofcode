def priority(c: str) -> int:
    if 'a' <= c <= 'z':
        return ord(c) - 96
    elif 'A' <= c <= 'Z':
        return ord(c) - 38
    
def day3(input):
    f = open(input, 'r')
    lines = f.readlines()

    #build dictionary
    ans = 0
    for line in lines:
        n = len(line)
        mid = n // 2
        set_left = set(line[:mid])
        set_right = set(line[mid:])
        for c in set_left:
            if c in set_right:
                ans += priority(c)
    print(ans)

day3('input.txt')
