import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        data = input().split()
        u_cnt = data[1].count('U')
        d_cnt = int(data[0]) - u_cnt
        tmp = d_cnt - u_cnt

        print((a[i] + tmp) % 10, end=' ')
    print()
