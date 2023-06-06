import sys

input = sys.stdin.readline

h, m = map(int, input().split(':'))
a = int(input())

t = h * 60 + m + a

print(f"{(t // 60) % 24:02}:{t % 60:02}")
