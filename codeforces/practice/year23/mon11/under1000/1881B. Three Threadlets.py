import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = sorted(map(int, input().split()))

    ans = True
    cnt = 0
    if data[1] % data[0] == 0 and data[2] % data[0] == 0:
        cnt += data[1] // data[0] - 1
        cnt += data[2] // data[0] - 1
    else:
        ans = False

    print("YES" if ans and cnt <= 3 else "NO")
