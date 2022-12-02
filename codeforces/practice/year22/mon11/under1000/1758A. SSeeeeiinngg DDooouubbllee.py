import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    print(data + data[::-1])
