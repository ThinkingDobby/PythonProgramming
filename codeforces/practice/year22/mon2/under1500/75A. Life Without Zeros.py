a = input()
b = input()

f = int(a) + int(b)
s = int(a.replace('0', '')) + int(b.replace('0', ''))
if str(f).replace('0', '') == str(s):
    print("YES")
else:
    print("NO")
