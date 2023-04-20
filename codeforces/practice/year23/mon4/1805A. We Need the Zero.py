import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = data[0]
    for i in range(1, n):
        tmp = data[i] ^ tmp

    if n % 2 == 0 and '1' in str(bin(tmp)[2:]):
        print(-1)
    else:
        print(tmp)
