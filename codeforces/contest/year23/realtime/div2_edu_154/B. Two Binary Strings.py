import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()

    ans = False
    for i in range(1, len(a)):
        if a[i - 1] == '0' and b[i - 1] == '0' and a[i] == '1' and b[i] == '1':
            ans = True
            break

    print("YES" if ans else "NO")