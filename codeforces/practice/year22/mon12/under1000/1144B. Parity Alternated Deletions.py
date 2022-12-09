import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

odds = sorted([i for i in data if i % 2 == 1])
evens = sorted([i for i in data if i % 2 == 0])

if len(odds) > len(evens):
    print(sum(odds[:max(0, len(odds) - len(evens) - 1)]))
else:
    print(sum(evens[:max(0, len(evens) - len(odds) - 1)]))

