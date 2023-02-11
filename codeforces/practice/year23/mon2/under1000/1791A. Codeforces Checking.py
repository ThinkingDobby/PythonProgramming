import sys

input = sys.stdin.readline

chk = set("codeforces")

for _ in range(int(input())):
    data = input().rstrip()
    print("YES" if data in chk else "NO")