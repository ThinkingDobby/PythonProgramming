import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

memo = [i for i in range(1, n - 1) if data[i - 1] < data[i] and data[i + 1] < data[i] or data[i - 1] > data[i] and data[i + 1] > data[i]]
print(len(memo))