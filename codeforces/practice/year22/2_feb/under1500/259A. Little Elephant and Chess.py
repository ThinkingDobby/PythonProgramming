data = [input() for i in range(8)]
flag = True
for i in data:
    if not(i == 'WBWBWBWB' or i == 'BWBWBWBW'):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
