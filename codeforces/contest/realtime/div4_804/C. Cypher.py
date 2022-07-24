import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        b, data = input().split()
        d_cnt = data.count('D')
        u_cnt = int(b) - d_cnt
        cnt = d_cnt - u_cnt
        tmp = a[i] + cnt
        if tmp >= 0:
            print((a[i] + cnt) % 10, end=' ')
        else:
            if tmp >= 0:
                print(tmp, end=' ')
            else:
                print(9 - ((abs(tmp) - 1) % 10), end=' ')
    print()