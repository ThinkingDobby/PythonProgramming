import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n == 1:
        print("NO")
    else:
        memo = [i for i in data if i != 1]
        ocnt = sum(data) - sum(memo)
        print("YES" if sum(data) - len(data) >= ocnt else "NO")
