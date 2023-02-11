import sys

input = sys.stdin.readline

n = int(input())
data = list(map(lambda x: ''.join(sorted(set(x))), input().split()))

print(len(set(data)))