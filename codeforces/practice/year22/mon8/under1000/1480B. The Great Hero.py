import sys

input = sys.stdin.readline

for _ in range(int(input())):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tot = sorted(zip(a, b))

    ans = True
    for i in range(n):
        tmp = (B + tot[i][0] - 1) // tot[i][0]
        lim = (tot[i][1] + A - 1) // A
        if tmp < lim:
            ans = False
            break
        else:
            B -= lim * tot[i][0]
            if B <= 0 and i != n - 1:
                ans = False
                break

    print("YES" if ans else "NO")
