import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = int(input())
    if str(data)[0] == '9':
        print(int('1' * (n + 1)) - data)
    else:
        print(10**n + 1 - data)