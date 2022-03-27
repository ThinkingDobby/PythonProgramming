import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()

cnt = data.count('0')
if '1' in data:
    print('1' + '0' * cnt)
else:
    print('0')