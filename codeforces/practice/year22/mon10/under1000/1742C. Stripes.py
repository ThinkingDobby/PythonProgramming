import sys

input = sys.stdin.readline

for _ in range(int(input())):
    input()
    data = [input().rstrip() for _ in range(8)]
    ans = "RRRRRRRR" in data

    print("R" if ans else "B")
