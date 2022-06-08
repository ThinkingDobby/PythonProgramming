import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    even_cnt = len([_ for i in data if i % 2 == 0])
    print(min(n - even_cnt, even_cnt))
