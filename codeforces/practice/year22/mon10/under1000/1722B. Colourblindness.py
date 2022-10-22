import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    f = input().rstrip().replace('G', '-').replace('B', '-')
    s = input().rstrip().replace('G', '-').replace('B', '-')

    print("YES" if f == s else "NO")