import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    minv = data[0]
    maxv = data[0]
    for i in range(1, n):
        minv = minv & data[i]
        maxv = maxv | data[i]

    print(maxv - minv)