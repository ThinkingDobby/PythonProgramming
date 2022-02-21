s = input()
fc = s.count('4')
sc = s.count('7')
if fc == 0 and sc == 0:
    print(-1)
else:
    print(4 if fc >= sc else 7)