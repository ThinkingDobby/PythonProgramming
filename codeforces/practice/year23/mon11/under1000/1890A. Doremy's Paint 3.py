import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = list(set(data))
    l = len(memo)

    if l == 1:
        print("YES")
    elif l == 2:
        if abs(data.count(memo[0]) - data.count(memo[1])) <= 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
