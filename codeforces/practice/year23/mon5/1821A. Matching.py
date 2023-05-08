import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    chk = data[0] == '?'
    ans = data[0] != '0'

    if not ans:
        print("0")
    else:
        cnt = list(data).count('?')
        print(10**cnt if not chk else 9 * 10**(cnt - 1))