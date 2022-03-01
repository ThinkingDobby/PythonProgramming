import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, a, b, c = map(int, input().split())
    tmp = s // c
    print(tmp + tmp // a * b)