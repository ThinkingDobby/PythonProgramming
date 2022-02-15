import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

data = input()
n = int(input())

if data == 'front':
    if n == 1:
        print('L')
    else:
        print('R')
else:
    if n == 1:
        print('R')
    else:
        print('L')
