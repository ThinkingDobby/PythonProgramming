import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().rstrip()))

    ans = ''
    i = n - 1
    while i >= 0:
        if i > 1 and data[i] == 0:
            ans += chr(data[i - 2] * 10 + data[i - 1] + 96)
            i -= 2
        else:
            ans += chr(data[i] + 96)
        i -= 1

    print(ans[::-1])

