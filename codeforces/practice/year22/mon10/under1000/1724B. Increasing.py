import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = set(map(int, input().split()))
    print("YES" if len(data) == n else "NO")