import sys

input = sys.stdin.readline

x = input().rstrip()
if x[0] =="a" or x[0] == "h" or x[1] == "1" or x[1] == "8":
    if x == "a1" or x == "a8" or x == "h1" or x == "h8":
        print(3)
    else:
        print(5)
else:
    print(8)