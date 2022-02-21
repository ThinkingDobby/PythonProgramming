n = int(input())
data = list(map(int, input().split()))
dict = {}
for i in range(n):
    dict[data[i]] = i + 1

order = list(map(lambda x: dict[int(x)], input().split()))

mv = 0
for i in order:
    if i < mv:
        print(0, end=' ')
    else:
        print(i - mv, end=' ')
        mv = i