n = int(input())

l = [str(i) if i > 9 else '0' + str(i) for i in range(0, 60) if '3' in str(i)]
tmp = len(l) * 60 * 2 - len(l) * len(l)

sum = 0
for i in range(n + 1):
    if '3' in str(i):
        sum += 60 * 60
    else:
        sum += tmp
print(sum)
