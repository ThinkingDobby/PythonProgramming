import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    print("NO" if len(set(data)) == 1 and data[0] == '1' else "YES")