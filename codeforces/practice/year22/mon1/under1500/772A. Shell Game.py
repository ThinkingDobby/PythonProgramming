a = "122100"
b = "001221"
c = "210012"

tmp = int(input()) % 6 - 1
data = input()
if data == a[tmp]:
    print(0)
elif data == b[tmp]:
    print(1)
else:
    print(2)