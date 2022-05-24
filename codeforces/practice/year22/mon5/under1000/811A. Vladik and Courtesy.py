import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
f = int(math.sqrt(a))
s = int(math.sqrt(b))
if s * (s + 1) > b:
    s -= 1

print("Vladik" if f <= s else "Valera")