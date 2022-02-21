mc = {'A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y'}
data = input()
flag = True
for i in data:
    if i not in mc:
        flag = False
        break

if flag and data == data[::-1]:
    print("YES")
else:
    print("NO")