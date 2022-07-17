import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    if n % 2 == 1:
        print("NO")
    else:
        ans = True
        for i in range(n // 2):
            if data[i] >= data[n // 2 + i]:
                ans = False
                break
            if i != n // 2 - 1:
                if data[n // 2 + i] <= data[i + 1]:
                    ans = False
                    break
        if data[0] >= data[-1]:
            ans = False

        if ans:
            print("YES")
            for i in range(n // 2):
                print(data[i], data[n // 2 + i], end=' ')
            print()
        else:
            print("NO")
