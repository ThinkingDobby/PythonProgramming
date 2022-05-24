import sys

input = sys.stdin.readline

memo = ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']
data = input().rstrip()
print(len([1 for i in data if i in memo]))