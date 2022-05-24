import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(lambda x: ord(x) - 96, list(input().rstrip())))
    s = sum(data)

    if len(data) % 2 == 0:
        print("Alice", s)
    else:
        if len(data) == 1:
            print("Bob", s)
        else:
            m = max(sum(data[1:]), sum(data[:-1]))
            print("Alice", 2 * m - s)
