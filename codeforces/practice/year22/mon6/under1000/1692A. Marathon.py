import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().split()))
    print(len([i for i in data[1:] if i > data[0]]))
