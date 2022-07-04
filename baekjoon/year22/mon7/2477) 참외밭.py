# WA

import sys

input = sys.stdin.readline

k = int(input())
data = [list(map(int, input().split()))[1] for _ in range(6)]

odds = sorted([data[i] for i in range(0, 6, 2)])
evens = sorted([data[i] for i in range(1, 6, 2)])



# memo = 0
# if data[0][0] == 4 and data[1][0] == 1:
#     memo = data[3][1] * data[4][1] - data[0][1] * data[1][1]
# else:
#     if data[2][0] == 4:
#         memo = data[4][1] * data[5][1] - data[1][1] * data[2][1]
#     else:
#         if data[3][0] == 2:
#             memo = data[0][1] * data[5][1] - data[2][1] * data[3][1]
#         else:
#             memo = data[0][1] * data[1][1] - data[3][1] * data[4][1]
#
# print(k * memo)

# if data[0] == data[2] + data[4] and data[1] == data[3] + data[5]:
#     print(k * (data[0] * data[1] - data[3] * data[4]))
# elif data[4] == data[0] + data[2] and data[3] == data[1] + data[5]:
#     print(k * (data[4] * data[3] - data[0] * data[1]))
# elif data[5] == data[1] + data[3] and data[4] == data[0] + data[2]:
#     print(k * (data[5] * data[4] - data[1] * data[2]))
# else:
#     print(k * (data[0] * data[5] - data[2] * data[3]))