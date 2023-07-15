import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = [True if data[i] % data[0] == 0 else False for i in range(1, n)]
    print("YES" if all(ans) else "NO")