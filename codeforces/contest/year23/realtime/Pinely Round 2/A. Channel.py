import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, q = map(int, input().split())

    data = input().rstrip()

    chk = a == n

    cnt = a
    for i in range(q):
        if data[i] == '+':
            cnt += 1
        else:
            cnt -= 1

        if cnt >= n:
            chk = True

    if chk:
        print("YES")
    else:
        print("MAYBE" if a + data.count('+') >= n else "NO")