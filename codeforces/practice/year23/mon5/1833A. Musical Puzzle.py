import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    memo = set()
    for i in range(1, n):
        memo.add(data[i - 1:i + 1])

    print(len(memo))