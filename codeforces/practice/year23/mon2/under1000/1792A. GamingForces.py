import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = data.count(1)
    print(tmp // 2 + tmp % 2 + n - tmp)