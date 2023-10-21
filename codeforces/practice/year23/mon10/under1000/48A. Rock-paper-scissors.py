import sys

input = sys.stdin.readline

data = [input().rstrip() for _ in range(3)]

memo = {0: 'F', 1: 'M', 2: 'S'}

tmp = list(set(data))
if len(tmp) in (1, 3):
    print('?')
else:
    if data.count(tmp[0]) == 1:
        one = tmp[0]
        twos = tmp[1]
    elif data.count(tmp[1]) == 1:
        one = tmp[1]
        twos = tmp[0]
    else:
        one = tmp[2]
        twos = tmp[0]

    if (one == "rock" and twos == "scissors") or (one == "paper" and twos == "rock") or (one == "scissors" and twos == "paper"):
        print(memo[data.index(one)])
    else:
        print('?')