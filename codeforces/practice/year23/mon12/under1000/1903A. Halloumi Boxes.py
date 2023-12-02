import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    chk = data == sorted(data)

    print("YES" if chk or k > 1 else "NO")