import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = True

    for i in range(1, n):
        if data[i - 1] > data[i]:
            if data[i] <= data[0]:
                if sorted(data) != data[i:] + data[:i]:
                    ans = False
                    break
            else:
                ans = False
                break

    print("YES" if ans else "NO")