n = int(input())
data = list(input())
gen = list(map(ord, ['A', 'C', 'T', 'G']))
memo = [0] * (n - 3)

for i in range(n - 3):
    for j in range(i, i + 4):
        memo[i] += min(abs(gen[j - i] - ord(data[j])),
                       abs(ord('Z') - ord(data[j])) + abs(ord('A') - gen[j - i]) + 1,
                       abs(ord('Z') - gen[j - i]) + abs(ord('A') - ord(data[j])) + 1)

print(min(memo))