import sys

input = sys.stdin.readline

n = int(input())
tmp = n * 60 * 60 + 59 * 60 + 59

cnt = 0
for i in range(tmp):
    h = i // (60 * 60)
    m = (i % (60 * 60)) // 60
    s = (i % (60 * 60)) % 60

    if '3' in str(h) or '3' in str(m) or '3' in str(s):
        cnt += 1

print(cnt)