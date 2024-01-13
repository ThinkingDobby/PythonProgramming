import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip())

    cnt = data.count('+')
    f, s = sorted([cnt, n - cnt])

    print(s - f)