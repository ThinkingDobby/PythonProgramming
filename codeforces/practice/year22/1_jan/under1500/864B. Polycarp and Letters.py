n = int(input())
data = list(input())

memo = set()
mv = 0
for i in range(n):
    if data[i].islower():
        if data[i] not in memo:
            memo.add(data[i])
    else:
        mv = max(len(memo), mv)
        memo.clear()
mv = max(len(memo), mv)

print(mv)
