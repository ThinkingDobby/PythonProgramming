import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data1 = set([input().rstrip() for _ in range(n)])
data2 = set([input().rstrip() for _ in range(m)])

tmp = data1 & data2
print(len(tmp))
for i in sorted(tmp):
    print(i)