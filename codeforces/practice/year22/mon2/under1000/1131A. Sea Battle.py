import sys

input = sys.stdin.readline

w1, h1, w2, h2 = map(int, input().split())
c1 = h2 * 2 + w2 + 2
c2 = h1 * 2 + w1 + 2
c3 = w1 - w2
print(c1 + c2 + c3)