import sys

input = sys.stdin.readline

data = input().rstrip()
piv = data.index('^')

left = data[:piv][::-1]
right = data[piv + 1:]

f = s = 0
for i in range(len(left)):
    if left[i].isdigit():
        f += (i + 1) * int(left[i])

for i in range(len(right)):
    if right[i].isdigit():
        s += (i + 1) * int(right[i])

if f == s:
    print("balance")
else:
    print("left" if f > s else "right")
