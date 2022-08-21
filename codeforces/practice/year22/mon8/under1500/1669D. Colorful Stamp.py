import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = set(input().rstrip().split('W')) - {''}

    ans = True
    for i in list(data):
        if len(set(i)) == 1:
            ans = False
            break

    print("YES" if ans else "NO")