import sys

input = sys.stdin.readline

for _ in range(int(input())):
    memo = {chr(i):0 for i in range(97, 123)}
    data = input().rstrip()

    for i in data:
        memo[i] += 1

    for i in range(len(data)):
        if memo[data[i]] == 1:
            print(data[i:])
            break
        else:
            memo[data[i]] -= 1
