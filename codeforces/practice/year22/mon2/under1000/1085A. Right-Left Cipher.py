import sys

input = sys.stdin.readline

data = input().rstrip()

tmp = (len(data) + 1) // 2
a = data[:tmp][::-1]
b = data[tmp:]

for i in range(tmp):
    print(a[i] + (b[i] if i < len(b) else ''), end='')
