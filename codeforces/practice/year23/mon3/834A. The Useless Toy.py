import sys

input = sys.stdin.readline

chk = ['v', '<', '^', '>']

a, b = input().split()
n = int(input())

ai = chk.index(a)
bi = chk.index(b)

chk = ai < bi
f = abs(ai - bi)
s = 4 - f

if (f - n) % 4 == 0 and (s - n) % 4 == 0:
    print("undefined")
elif (f - n) % 4 == 0:
    print("cw" if chk else "ccw")
elif (s - n) % 4 == 0:
    print("ccw" if chk else "cw")
else:
    print("undefined")
