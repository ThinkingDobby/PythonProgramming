import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    cnt = a

    if b % 3 != 0 and b % 3 + c < 3:
        print(-1)
    else:
        cnt += (b + c + 2) // 3
        print(cnt)