import sys

input = sys.stdin.readline

ch, cm = map(int, input().split(':'))
sh, sm = map(int, input().split(':'))

tmp = ch * 60 + cm - (sh * 60 + sm)
while tmp < 0:
    tmp = 24 * 60 + tmp

print("{:02}".format(tmp // 60) + ":" + "{:02}".format(tmp % 60))