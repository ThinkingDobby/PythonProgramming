import sys

input = sys.stdin.readline

data = input().rstrip()

if len(data) < 5 or not any([True if i.isupper() else False for i in data]) \
        or not any([True if i.islower() else False for i in data]) \
        or not any([True if i.isdigit() else False for i in data]):
    print("Too weak")
else:
    print("Correct")
