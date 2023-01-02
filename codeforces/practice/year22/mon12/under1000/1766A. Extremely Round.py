import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = int(input())
    tmp = str(data)[1:]
    print(int(str(data)[0]) + len(tmp) * 9)
