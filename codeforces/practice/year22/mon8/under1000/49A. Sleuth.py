import sys

input = sys.stdin.readline

data = input().rstrip()
last = ''
for i in range(len(data) - 1, -1, -1):
    if data[i].isalpha():
        last = data[i]
        break

print("YES" if last.lower() in ['a', 'e', 'i', 'o', 'u', 'y'] else 'NO')