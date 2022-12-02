import sys

input = sys.stdin.readline

n, a, x, b, y = map(int, input().split())

a -= 1
b -= 1
x -= 1
y -= 1

ans = False
while True:
    if a == b:
        ans = True
    if a == x or b == y:
        break
    a = (a + 1) % n
    b = (b - 1) % n

print("YES" if ans else "NO")