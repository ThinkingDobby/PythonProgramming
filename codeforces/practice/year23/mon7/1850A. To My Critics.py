import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = sorted(map(int, input().split()))
    print("YES" if data[1] + data[2] >= 10 else "NO")
