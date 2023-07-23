import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
sdata = sorted(data)

if n > 1 and sdata[0] == sdata[1]:
    print("Still Rozdil")
else:
    print(data.index(sdata[0]) + 1)