import sys

input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]
memo = [sum(i) * 5 + len(i) * 15 for i in data]

print(min(memo))
