import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    data = [sorted(map(int, input().split())) for _ in range(n)]
    print("YES" if k in set(i[0] for i in data).intersection(set(i[1] for i in data)) else "NO")
