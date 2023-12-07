import sys

input = sys.stdin.readline

nums = list([str(i) for i in range(1, 9)])
chrs = list([chr(i) for i in range(97, 105)])

for _ in range(int(input())):
    data = input().rstrip()

    for i in nums:
        if i != data[1]:
            print(data[0] + i)

    for i in chrs:
        if i != data[0]:
            print(i + data[1])
