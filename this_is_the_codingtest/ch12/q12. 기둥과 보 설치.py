def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


# def solution(n, build_frame):
#     n += 1
#     memo = [[0] * n for _ in range(n)]
#     for x, y, a, b in build_frame:
#         if b == 0:
#             if a == 0:
#                 if not(memo[x - 1][y + 1] < 2 and memo[x][y + 1] % 2 == 1 and memo[x][y + 1] < 2) and not (
#                         memo[x + 1][y] % 2 != 1 and memo[x][y + 1] > 1 and (memo[x - 1][y + 1] < 2 or memo[x + 1][y + 1] < 2)):
#                     memo[x][y] -= 1
#             else:
#                 if not (memo[x - 1][y] < 2 and memo[x][y] % 2 == 1) and not (
#                         memo[x + 1][y] % 1 == 1 and memo[x + 1][y] < 2) and not (
#                         memo[x - 1][y - 1] % 2 != 1 and memo[x - 1][y] > 1) and not (
#                         memo[x + 2][y - 1] % 2 != 1 and memo[x + 1][y] > 1):
#                     memo[x][y] -= 2
#         else:
#             if a == 0:
#                 if y == 0 or memo[x][y - 1] % 2 == 1 or ((memo[x - 1][y] > 1) ^ (memo[x][y] > 1)):
#                     memo[x][y] += 1
#             else:
#                 if memo[x][y - 1] % 2 == 1:
#                     memo[x][y] += 2
#                     continue
#                 if x + 1 < n:
#                     if memo[x + 1][y - 1] % 2 == 1:
#                         memo[x][y] += 2
#                     elif memo[x - 1][y] > 1 and memo[x + 1][y] > 1:
#                         memo[x][y] += 2
#
#     ans = []
#     for i in range(n):
#         for j in range(n):
#             print(memo[i][j], end=' ')
#             if memo[i][j] == 3:
#                 ans.append([i, j, 0])
#                 ans.append([i, j, 1])
#             elif memo[i][j] == 2:
#                 ans.append([i, j, 1])
#             elif memo[i][j] == 1:
#                 ans.append([i, j, 0])
#         print()
#
#     return ans


ans = solution(5,[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
for i in ans:
    print(i)
