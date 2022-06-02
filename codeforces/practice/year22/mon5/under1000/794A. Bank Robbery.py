import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
n = int(input())
data = list(map(int, input().split()))
print(len([i for i in data if b < i < c]))