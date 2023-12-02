def day2(input):
    ans = 0
    f = open(input)

    for line in f.read().split('\n'):
        t = line.split(':')
        games = t[1].split(';')
        id = t[0].split(' ')[1]
        cubedict = {'red':0, 'blue':0, 'green':0}
        
        for game in games:
            cubes = game.split(',')
            #print(cubes)
            for cube in cubes:
                cube = cube.split(' ')
                #print(cube)
                num = int(cube[1])
                colour = cube[2]
                #print(num, colour)
                if cubedict[colour] < num:
                    cubedict[colour] = num
            
        #print(id, cubedict)
        prod = cubedict['red'] * cubedict['green'] * cubedict['blue']
        ans += prod
    print(ans)
    return ans

day2('input.txt')
