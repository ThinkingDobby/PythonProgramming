import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(9, 0, -1):
        tmp = n - i
        if tmp < 0:
            ans.append(n)
            break
        else:
            n -= i
            ans.append(i)

    s = ''
    for i in ans[::-1]:
        s += str(i)
    print(int(s))