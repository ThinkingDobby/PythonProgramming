import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    c = input().rstrip()

    flag = False

    for i in range(len(data)):
        if i % 2 == 0 and data[i] == c:
            flag = True
            break

    print("YES" if flag else "NO")