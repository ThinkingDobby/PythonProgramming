import sys

input = sys.stdin.readline

n, m = map(int, input().split())

memo = ['' for i in range(n)]
memo_num = dict()

for i in range(n):
    name = input().rstrip()
    memo[i] = name
    memo_num[name] = i + 1

for _ in range(m):
    data = input().rstrip()
    if str.isdigit(data):
        print(memo[int(data) - 1])
    else:
        print(memo_num[data])
