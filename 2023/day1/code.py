def day1(input):
    f = open(input)
    ans = 0

    for line in f.read().split('\n'):
        n = []
        for i in range(len(line)):
            if not line[i].isalpha():
                n.append(line[i])

        if len(n) > 0:
            first = n[0]
            last = n[-1]
            ans += int(first) * 10 + int(last)
            #print(int(n))

    print(ans)
    return ans

day1('input.txt')
