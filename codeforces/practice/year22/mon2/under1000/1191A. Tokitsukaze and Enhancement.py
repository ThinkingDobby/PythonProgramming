n = int(input())
tmp = n % 4

if tmp == 1:
    print(0, 'A')
elif tmp == 3:
    print(2, 'A')
elif tmp == 2:
    print(1, 'B')
else:
    print(1, 'A')