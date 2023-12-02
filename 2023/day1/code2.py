def part2(input):
    f = open(input)
    ans = 0

    d = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    words = set(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    initials = set('ottffssen')

    for line in f.read().split('\n'):
        n = []
        for i in range(len(line)):
            if not line[i].isalpha():
                n.append(line[i])
            else:
                t = ""
                if line[i] in initials:
                    for j in range(5):
                        if i+j < len(line):
                            t += line[i+j]
                            if t in words:
                                print(t)
                                n.append(d[t])
                                break
                    #print(t)
                    t = ""
                
        if len(n) > 0:
            first = n[0]
            last = n[-1]
            ans += int(first) * 10 + int(last)
            #print(int(n))

    print(ans)
    return ans

part2('input.txt')
