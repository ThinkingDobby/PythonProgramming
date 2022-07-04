import collections
import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = [(int(input())) for _ in range(n)]

memo = [0] * (k + 1)

for i in data:
    memo[i] += 1
    for j in range(i + 1, k + 1):
        if j % i == 0:
            cnt = 0
            for k in range(i, j + 1, i):
                if j - k != i and memo[j - k] > 0:
                    cnt += 1
            memo[j] += cnt

print(memo)






#
# for i in range(2, k + 1):
#     for j in range(1, int(math.sqrt(i)) + 1):
#         if memo[i // j] > 0:
#             if i % j != 0:
#                 if memo[i % j] > 0:
#                     memo[i] += (memo[i // j] + memo[i % j])
#             else:
#                 memo[i] += memo[i // j]
#         print(i, j, memo[i])
#
# print(memo)
#
