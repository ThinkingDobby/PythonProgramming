import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().rstrip()))
    print("YES" if sum(data[:3]) == sum(data[3:]) else "NO")