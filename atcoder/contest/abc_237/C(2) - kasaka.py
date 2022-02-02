data = input()
tmp = data.rstrip('a')
suffix = len(data) - len(tmp)
sdata = tmp.lstrip('a')
prefix = len(tmp) - len(sdata)

if sdata == sdata[::-1] and prefix <= suffix:
    print("Yes")
else:
    print("No")