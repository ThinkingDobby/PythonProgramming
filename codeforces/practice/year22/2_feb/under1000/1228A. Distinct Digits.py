l, r = map(int, input().split())
flag = False
for i in range(l, r + 1):
    tmp = str(i)
    if len(set(tmp)) == len(tmp):
        print(i)
        flag = True
        break

if not flag:
    print(-1)