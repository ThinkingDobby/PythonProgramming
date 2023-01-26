import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

tmp = 1
while tmp <= m and n > 0:
    tmp *= 2
    n -= 1

print(m % tmp)