import sys

input = sys.stdin.readline

pv = set(input().split())
print(*pv)

for _ in range(int(input())):
    a, b = input().split()
    pv.remove(a)
    pv.add(b)
    print(*pv)
