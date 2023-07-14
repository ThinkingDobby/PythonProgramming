import sys

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

ans = True
prev = 1 if data[0] == 2 else 2
prev_idx = -1

if data[0] == 3:
    ans = False
else:
    for i in range(1, n):
        if data[i - 1] != data[i]:
            tmp = i - prev_idx - 1
            if tmp % 2 == 0:
                if prev != data[i]:
                    ans = False
                    break
            else:
                if prev == data[i]:
                    ans = False
                    break

            prev_idx = i - 1
            prev = data[i - 1]

print("YES" if ans else "NO")