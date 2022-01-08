import sys

for _ in range(int(input())):
    n, k, d = map(int, input().split())
    data = list(map(int, input().split()))

    mv = sys.maxsize
    for i in range(0, n - d + 1):
        mv = min(mv, len(set(data[i:i + d])))

    print(mv)