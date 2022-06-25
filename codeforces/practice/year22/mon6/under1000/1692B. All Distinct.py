import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = len(set(data))
    print(tmp - 1 if (n - tmp) % 2 == 1 else tmp)