import sys

input = sys.stdin.readline

mod = 796_796

n = int(input())
memo = [0] * (n + 1)
memo[1] = 1
memo[2] = 3

for i in range(3, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2] * 2) % mod

print(memo[n])