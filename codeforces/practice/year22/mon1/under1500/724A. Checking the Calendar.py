a = input()
b = input()

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

flag = False
for i in [28, 30, 31]:
    if days[(days.index(a) + i) % 7] == b:
        flag = True

if flag:
    print("YES")
else:
    print("NO")