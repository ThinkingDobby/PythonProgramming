import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = input().rstrip()

for _ in range(m):
    l, r, c1, c2 = input().rstrip().split()
    for i in range(int(l) - 1, int(r)):
        if data[i] == c1:
            data = data[:i] + c2 + data[i + 1:]

print("".join(data))
