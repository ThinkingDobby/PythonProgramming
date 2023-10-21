import sys

input = sys.stdin.readline

data = input().rstrip()
memo = [input().rstrip() for _ in range(10)]

for i in range(0, 71, 10):
    tmp = memo.index(data[i:i + 10])
    print(tmp, end='')
