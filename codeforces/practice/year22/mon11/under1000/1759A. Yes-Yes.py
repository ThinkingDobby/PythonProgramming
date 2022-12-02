import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    check = ['Y', 'e', 's']

    ans = True
    if data[0] in check:
        now = check.index(data[0])
        for i in range(0, len(data)):
            if data[i] != check[now]:
                ans = False
                break
            now = (now + 1) % 3
    else:
        ans = False

    print("YES" if ans else "NO")