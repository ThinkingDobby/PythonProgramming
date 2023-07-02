import sys

input = sys.stdin.readline

weights = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0, '.': 0}

data = [input().rstrip() for _ in range(8)]

f = 0
s = 0

for i in data:
    for j in i:
        if j.islower():
            s += weights[j.upper()]
        else:
            f += weights[j]

if f == s:
    print("Draw")
else:
    print("White" if f > s else "Black")