import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    left_cnt = right_cnt = 0

    n = len(data)
    result = '(' * n + ')' * n
    if data in result:
        result = "()" * n
        if data in result:
            print("NO")
        else:
            print("YES")
            print(result)
    else:
        print("YES")
        print(result)