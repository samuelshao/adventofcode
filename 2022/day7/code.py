import re

def day7(input):
    lines = list(open(input))
    
    for line in lines:
        cmd = re.findall('^$', line)
        print(cmd)

day7('input.txt')
