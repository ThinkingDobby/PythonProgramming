import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip().lower()

    tmp = data[0]

    for i in range(1, n):
        if data[i] != data[i - 1]:
            tmp += data[i]

    print("YES" if tmp == "meow" else "NO")