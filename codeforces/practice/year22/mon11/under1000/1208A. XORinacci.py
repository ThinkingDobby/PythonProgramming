import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    data = [0] * 3
    data[0] = a ^ b
    data[1] = b ^ data[0]
    data[2] = data[0] ^ data[1]

    print(data[(n + 1) % 3])