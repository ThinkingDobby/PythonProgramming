import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    print("YES" if data[0] == 'a' or data[1] == 'b' or data[2] == 'c' else "NO")