import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
mv = max(data)
print(sum([i / mv * 100 for i in data]) / n)