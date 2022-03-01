import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = input().rstrip()
memo = [data.count(chr(i)) for i in range(65, 65 + k)]
print(min(memo) * k)