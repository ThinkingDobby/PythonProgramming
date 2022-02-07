n = int(input())
memo = [['x'] * (n + 2)]
for _ in range(n):
    memo.append(['x'] + list(input()) + ['x'])
memo.append(['x'] * (n + 2))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

flag = True
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt = 0
        for k in move:
            if memo[i + k[0]][j + k[1]] == 'o':
                cnt += 1
        if cnt % 2 == 1:
            flag = False
            break

if flag:
    print("YES")
else:
    print("NO")