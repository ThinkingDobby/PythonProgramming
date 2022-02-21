n = int(input())
data = input()

cnt = data.count('I')
if cnt > 1:
    print(0)
elif cnt == 1:
    print(1)
else:
    print(data.count('A'))