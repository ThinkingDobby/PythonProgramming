import sys

input = sys.stdin.readline

memo = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

data = input().rstrip()
n = int(input())

tmp = memo.index(data)
ans = memo[(tmp + n) % 12]

print(ans)