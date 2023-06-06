import sys

input = sys.stdin.readline

a = input().rstrip().lstrip("0")
b = input().rstrip().lstrip("0")

if len(a) == len(b):
    if a == b:
        print("=")
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                print(">" if a[i] > b[i] else "<")
                break
elif len(a) > len(b):
    print(">")
else:
    print("<")