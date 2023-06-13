import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

memo = ''.join(map(str, data)).strip('0')

while '101' in memo:
    memo = memo.replace('101', '111')

memo = memo.split('0')
print(sum(map(lambda x: len(x), memo)))
