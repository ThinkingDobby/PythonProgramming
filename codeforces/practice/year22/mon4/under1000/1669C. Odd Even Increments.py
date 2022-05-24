import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    f = all(map(lambda x: x % 2 == 0, data[0:n:2])) or all(map(lambda x: x % 2 == 1, data[0:n:2]))
    s = all(map(lambda x: x % 2 == 0, data[1:n:2])) or all(map(lambda x: x % 2 == 1, data[1:n:2]))

    print("YES" if f and s else "NO")