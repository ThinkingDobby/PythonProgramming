import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for _ in range(3):
    f, s = map(int, input().split())
    if n == f:
        n = s
    elif n == s:
        n = f

print(n)