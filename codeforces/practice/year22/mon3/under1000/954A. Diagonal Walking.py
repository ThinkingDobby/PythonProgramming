import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()

i = 0
cnt = 0
while True:
    if i >= n - 1:
        break
    if data[i] == 'R' and data[i + 1] == 'U' or data[i] == 'U' and data[i + 1] == 'R':
        cnt += 1
        i += 1
    i += 1

print(n - cnt)