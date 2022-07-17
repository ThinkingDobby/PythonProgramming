import sys

input = sys.stdin.readline

n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

f = 0
s = 0
tf = 0
ts = 0
for i in range(n):
    tf += t[i]
    ts += t[n - 1 - i]
    f += max(p[i] - c * tf, 0)
    s += max(p[n - 1 - i] - c * ts, 0)

if f > s:
    print("Limak")
elif f == s:
    print("Tie")
else:
    print("Radewoosh")