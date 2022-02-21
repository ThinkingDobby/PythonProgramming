move = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
n = int(input())
data = input()
memo = {(0, 0): 1}
s = 0

cur = (0, 0)
for i in range(n):
    cur = (cur[0] + move[data[i]][0], cur[1] + move[data[i]][1])
    if cur in memo:
        s += memo[cur]
        memo[cur] += 1
    else:
        memo[cur] = 1

print(s)