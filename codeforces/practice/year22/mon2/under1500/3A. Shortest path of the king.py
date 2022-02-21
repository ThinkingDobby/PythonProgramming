x1, y1 = input()
x2, y2 = input()

xcnt = ord(x1) - ord(x2)
ycnt = int(y1) - int(y2)

memo = []
while xcnt or ycnt:
    ans = ''

    if xcnt < 0:
        ans += 'R'
        xcnt += 1
    elif xcnt > 0:
        ans += 'L'
        xcnt -= 1

    if ycnt < 0:
        ans += 'U'
        ycnt += 1
    elif ycnt > 0:
        ans += 'D'
        ycnt -= 1

    memo.append(ans)

print(len(memo))
for i in memo:
    print(i)