import sys

input = sys.stdin.readline

for i in range(int(input())):
    data = list(input().rstrip())

    l = len(data)
    if l % 2 == 1:
        print("YES" if len(set(data[:l // 2] + data[l // 2 + 1:])) >= 2 else "NO")
    else:
        print("YES" if len(set(data)) >= 2 else "NO")