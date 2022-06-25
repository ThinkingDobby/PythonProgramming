import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = sorted(input().rstrip())
    b = sorted(input().rstrip())

    a_cnt = 0
    b_cnt = 0
    i = j = 0

    while i < n and j < m:
        if a_cnt < k:
            if b_cnt < k and a[i] > b[j]:
                print(b[j], end='')
                b_cnt += 1
                a_cnt = 0
                j += 1
            else:
                print(a[i], end='')
                a_cnt += 1
                b_cnt = 0
                i += 1
        else:
            print(b[j], end='')
            b_cnt += 1
            a_cnt = 0
            j += 1
    print()
