import sys

input = sys.stdin.readline

chk = set("Timur")

for _ in range(int(input())):
    n = int(input())
    data = set(input().rstrip())
    print("YES" if data == chk and n == 5 else "NO")
