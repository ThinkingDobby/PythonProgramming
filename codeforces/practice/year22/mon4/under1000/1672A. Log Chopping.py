import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = sum(map(lambda x: int(x) - 1, input().split()))
    print("errorgorn" if s % 2 == 1 else "maomao90")