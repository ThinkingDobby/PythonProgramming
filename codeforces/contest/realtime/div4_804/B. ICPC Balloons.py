import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    tmp = len(set(data))
    print(tmp * 2 + n - tmp)