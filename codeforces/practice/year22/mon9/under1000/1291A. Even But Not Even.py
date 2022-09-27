import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().rstrip()))

    tmp = [i for i in data if i % 2 == 1]
    if len(tmp) < 2:
        print(-1)
    else:
        print(''.join(map(str, tmp[:2])))
