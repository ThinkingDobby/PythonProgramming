import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if sum(x) < sum(y):
    print("No")
else:
    print("YES")