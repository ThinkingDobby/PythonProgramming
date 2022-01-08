# 미완성

# for t in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split(" ")))
#     m = 0
#     for i in range(1, n - 1):
#         for s in range(1, n - 1):
#             tmp = {}
#             for j in range(i, n - s, s):
#                 try:
#                     tmp[a[i] - a[i + s]] = tmp[a[i] - a[i + s]] + 1
#                 except:
#                     tmp[a[i] - a[i + s]] = 1
#             m = max(m, max(tmp.values()) if tmp.values() else 0)
#     print(n - (m + 1))