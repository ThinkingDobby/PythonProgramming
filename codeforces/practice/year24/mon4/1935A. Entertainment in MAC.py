import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    data = input().rstrip()

    if data > data[::-1]:
        print(data[::-1] + data)
    else:
        print(data)
