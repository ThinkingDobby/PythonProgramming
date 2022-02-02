flag = False
check = False
cnt = 0

data = list(input())
for i in range(len(data)):
    if data[i] == '1':
        check = True
    if check and data[i] == '0':
        cnt += 1
    if cnt == 6:
        flag = True
        break

if flag:
    print("yes")
else:
    print("no")