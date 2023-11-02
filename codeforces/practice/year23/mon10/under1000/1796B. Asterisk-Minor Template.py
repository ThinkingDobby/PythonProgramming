import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()

    if a[0] == b[0]:
        print("YES")
        print(a[0] + '*')
    elif a[-1] == b[-1]:
        print("YES")
        print('*' + a[-1])
    else:
        ans = False
        for i in range(len(a) - 1):
            for j in range(len(b) - 1):
                if a[i:i + 2] == b[j:j + 2]:
                    print("YES")
                    print('*' + a[i:i + 2] + '*')
                    ans = True
                    break
            if ans:
                break

        if not ans:
            print("NO")