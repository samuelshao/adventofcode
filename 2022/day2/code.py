import re

def strategy(input):
    #rock: A, X; paper: B, Y; scissors: C, Z
    d = {
        "A X":4,
        "A Y":8,
        "A Z":3,
        "B X":1,
        "B Y":5,
        "B Z":9,
        "C X":7,
        "C Y":2,
        "C Z":6
    }

    d2 = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
        }
    f = open(input, 'r')
    lines = f.readlines()
    score = 0
    for line in lines:
        chars = []
        for c in line:
            if c.isalpha():
                chars.append(c)
        strat = chars[0] + ' ' + chars[1]
        #print(strat)
        score += d2[strat]
    print(score)
strategy('input.txt')
