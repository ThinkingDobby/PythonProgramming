import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    sd = sorted(data)

    print(len([i for i in range(n) if data[i] != sd[i]]) // 2)
