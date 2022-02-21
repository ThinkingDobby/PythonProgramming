n = int(input())
data = input()

memo = [False] * 10

for i in data:
    if i == 'L':
        for j in range(10):
            if not memo[j]:
                memo[j] = True
                break
    elif i == 'R':
        for j in range(9, -1, -1):
            if not memo[j]:
                memo[j] = True
                break
    else:
        memo[int(i)] = False

print("".join(['1' if i else '0' for i in memo]))