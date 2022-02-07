n = int(input())
data = [list(input()) for _ in range(n)]

cd = data[0][0]
co = data[0][1]

flag = True
if cd == co:
    flag = False
else:
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                if data[i][j] != cd:
                    flag = False
                    break
            else:
                if data[i][j] != co:
                    flag = False
                    break

if flag:
    print("YES")
else:
    print("NO")