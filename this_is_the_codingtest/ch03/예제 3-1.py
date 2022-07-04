n = int(input())
cnt = 0
coins = [500, 100, 50, 10]

for i in coins:
    cnt += n // i
    n %= i

print(cnt)

# import sys
#
# n = int(input())
# ans = sys.maxsize
#
# coins = [500, 400, 100]
#
# for t in range(len(coins)):
#     cnt = 0
#     tmp = n
#     for i in range(t, len(coins)):
#         cnt += tmp // coins[i]
#         tmp %= coins[i]
#     ans = min(ans, cnt)
#
# print(ans)
