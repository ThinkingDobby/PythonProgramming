import sys

input = sys.stdin.readline

n, q = map(int, input().split())
data = input()
cnt = data.count('abc')
data = list(data)

for _ in range(q):
    i, c = input().split()
    i = int(i) - 1

    prev = data[i]
    if prev != c:
        if 'abc' in ''.join(data[max(0, i - 2):i + 3]):
            cnt -= 1
        data[i] = c
        if 'abc' in ''.join(data[max(0, i - 2):i + 3]):
            cnt += 1

    print(cnt)