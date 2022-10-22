import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().split()))

    ans = False
    for i in data:
        if i == sum(data) - i:
            ans = True

    print("YES" if ans else "NO")
