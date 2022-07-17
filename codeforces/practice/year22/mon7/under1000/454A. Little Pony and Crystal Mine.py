import sys

input = sys.stdin.readline

n = int(input())
cnt = 1
for i in range(n):
    tmp = '*' * ((n - cnt) // 2)
    print(tmp + 'D' * cnt + tmp)
    if i >= n // 2:
        cnt -= 2
    else:
        cnt += 2