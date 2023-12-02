#print(max([sum(list(map(int,line.split()))) for line in open('input.txt').read().split('\n\n')]))

def caloriecount(input):
    f = open(input)
    calorielist = []
    for line in f.read().split('\n\n'):
        calorielist.append(sum(list(map(int, line.split()))))
    
    calorielist.sort(reverse=True)
    print(sum(calorielist[:3]))

caloriecount('input.txt')