import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    chk = [i for i in data if i % 2 == 0]
    if len(chk) == n or len(chk) == 0:
        print("YES")
    else:
        print("YES" if min(data) != min(chk) else "NO")