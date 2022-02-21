import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = data[0]
    for i in range(1, n):
        tmp = tmp | data[i]
    print(tmp)