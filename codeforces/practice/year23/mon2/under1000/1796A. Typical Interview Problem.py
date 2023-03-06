import sys

input = sys.stdin.readline

s = 'FBFBFFBFFBFBFFBFFBFBFFBFF'

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    print("YES" if data in s else "NO")