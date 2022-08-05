import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input().rstrip()
    b = input().rstrip()
    if m == 1:
        print("YES" if b in a else "NO")
    else:
        if a[-(len(b) - 1):] == b[1:] and b[0] in a[:-(len(b) - 1)]:
            print("YES")
        else:
            print("NO")