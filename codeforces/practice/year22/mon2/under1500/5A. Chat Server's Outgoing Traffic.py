import sys

cnt = 0
num = 0

for data in sys.stdin.readlines():
    data = data.rstrip()
    if data[0] == '+':
        num += 1
    elif data[0] == '-':
        num -= 1
    else:
        tmp = len(data[data.index(':') + 1:]) * num
        cnt += tmp

print(cnt)