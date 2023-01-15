import sys

input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))

i = 0
tot = sum(data)
while n * 4.5 - tot > 0:
    tot += 5 - data[i]
    i += 1

print(i)