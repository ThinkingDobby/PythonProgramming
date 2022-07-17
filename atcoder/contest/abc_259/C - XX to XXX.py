import sys

input = sys.stdin.readline

f = list(input().rstrip()) + ['*']
s = list(input().rstrip()) + ['*']

f_memo = []
s_memo = []

cnt = 1
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        f_memo.append([f[i], cnt])
        cnt = 1
    else:
        cnt += 1

cnt = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        s_memo.append([s[i], cnt])
        cnt = 1
    else:
        cnt += 1

if len(f_memo) == len(s_memo):
    ans = True
    for i in range(len(f_memo)):
        if f_memo[i][0] == s_memo[i][0]:
            t1 = f_memo[i][1]
            t2 = s_memo[i][1]
            if t1 != t2:
                if (t1 == 1 and t1 < t2) or t1 > t2:
                    ans = False
                    break
        else:
            ans = False
            break
    print("Yes" if ans else "No")
else:
    print("No")


# f = ['*'] + list(input().rstrip()) + ['*']
# s = ['*'] + list(input().rstrip()) + ['*']
#
# f_memo = []
# s_memo = []
#
# for i in range(1, len(f) - 1):
#     if f[i - 1] != f[i]:
#         if f[i] != f[i + 1]:
#             f_memo.append(f[i] * 2)
#         else:
#             f_memo.append(f[i])
#
# for i in range(1, len(s) - 1):
#     if s[i - 1] != s[i]:
#         if s[i] != s[i + 1]:
#             s_memo.append(s[i] * 2)
#         else:
#             s_memo.append(s[i])
#
# if len(f_memo) == len(s_memo):
#     print("Yes" if all([f_memo[i] == s_memo[i] for i in range(len(f_memo))]) else "No")
# else:
#     print("No")
#
#
