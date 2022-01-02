iv = input("Enter FullName: ").split()
memo = [(i, len(i)) for i in iv]
check = sorted([i[1] for i in memo], reverse=True)[:4]

print("출력결과: ", end='')
for i in iv:
    if len(i) in check:
        print(i[0].upper(), end='')
        check.remove(len(i))