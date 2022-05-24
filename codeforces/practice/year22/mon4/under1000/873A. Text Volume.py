import sys

input = sys.stdin.readline

n = int(input())
data = list(input().rstrip().split(" "))

mv = -1
for i in data:
    mv = max(mv, len([j for j in i if j.isupper()]))

print(mv)
