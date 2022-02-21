u = int(input())
d = int(input())

tot = u + d + 1

for i in range(tot, tot - d, -1):
    print(i, end=' ')
for i in range(1, tot - d + 1):
    print(i, end=' ')