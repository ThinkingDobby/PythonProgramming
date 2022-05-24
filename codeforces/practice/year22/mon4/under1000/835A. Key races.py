import sys

input = sys.stdin.readline

s, v1, v2, t1, t2 = map(int, input().split())
fv = v1 * s + t1 * 2
sv = v2 * s + t2 * 2

if fv < sv:
    print("First")
elif fv > sv:
    print("Second")
else:
    print("Friendship")