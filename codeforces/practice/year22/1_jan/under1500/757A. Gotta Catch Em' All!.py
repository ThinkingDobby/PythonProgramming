now = 0
target = "auBlbsr"
memo = [0] * 7

data = list(input())

cnt = 0
for i in range(len(data)):
    for j in range(len(target)):
        if data[i] == target[j]:
            memo[j] += 1

memo[0] //= 2
memo[1] //= 2
print(min(memo))