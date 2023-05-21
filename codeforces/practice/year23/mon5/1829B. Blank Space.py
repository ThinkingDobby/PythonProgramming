import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip().replace(' ', '').split('1'))
    mv = max(map(lambda x: len(x), data))

    print(mv)