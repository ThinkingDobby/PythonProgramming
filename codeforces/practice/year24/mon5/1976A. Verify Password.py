import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip())

    ans = True

    ac = False
    idx = n

    for i in range(len(data)):
        if str.isdigit(data[i]):
            if ac:
                ans = False
                break
        else:
            if not ac:
                ac = True
                idx = i

    if not sorted(data[:idx]) == data[:idx] or not sorted(data[idx:]) == data[idx:]:
        ans = False

    print("YES" if ans else "NO")
