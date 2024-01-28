import sys

input = sys.stdin.readline

data = input().split()

if data[2] == "week":
    if data[0] == "5" or data[0] == "6":
        print(53)
    else:
        print(52)
else:
    if data[0] == "30":
        print(11)
    elif data[0] == "31":
        print(7)
    else:
        print(12)
