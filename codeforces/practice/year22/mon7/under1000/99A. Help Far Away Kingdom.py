import sys

input = sys.stdin.readline

n = input().rstrip()
idx = n.index('.')
if n[idx - 1] == '9':
    print("GOTO Vasilisa.")
else:
    if int(n[idx + 1]) < 5:
        print(n[:idx])
    else:
        print(int(n[:idx]) + 1)