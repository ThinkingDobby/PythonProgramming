import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = [1, 4] + [4 * 3**i for i in range(1,n - 1)]
    if ans[-1] > 10 ** 9:
        print("NO")
    else:
        print("YES")
        print(*ans)