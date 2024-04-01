import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n == 1:
        print("YES")
    else:
        s = 0
        while s < n - 2 and data[s] == data[s + 1]:
            s += 1

        ans = True
        inc = data[s] < data[s + 1]

        for i in range(s, n - 1):
            if data[i] > data[i + 1] and inc:
                inc = False

            if not inc and data[i] < data[i + 1]:
                ans = False
                break

        print("YES" if ans else "NO")
