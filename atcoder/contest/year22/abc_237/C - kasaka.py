data = input()
sdata = data.rstrip('a')
idx = -1
cnt = len(data) - len(sdata)

for i in range(len(sdata)):
    if cnt != 0 and sdata[i] == 'a':
        idx = i
        cnt -= 1
    else:
        break

if sdata[idx + 1:] == sdata[idx + 1:][::-1]:
    print("Yes")
else:
    print("No")