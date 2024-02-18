import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = [1, 1, 1]

    n -= 3
    for i in range(2, -1, -1):
        tmp = min(25, n)
        n -= tmp
        ans[i] += tmp

    print(''.join(map(lambda x: chr(96 + x), ans)))