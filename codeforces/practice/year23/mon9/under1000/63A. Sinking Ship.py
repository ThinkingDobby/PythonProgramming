import sys

input = sys.stdin.readline

priority = {"rat": 0, "woman": 1, "child": 1, "man": 2, "captain": 3}

n = int(input())
data = [input().rstrip().split() for _ in range(n)]
sdata = sorted(data, key=lambda x: priority[x[1]])

for i, j in sdata:
    print(i)
