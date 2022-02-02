import math

for _ in range(int(input())):
    hc, dc = map(int, input().split())
    hm, dm = map(int, input().split())
    k, w, a = map(int, input().split())

    flag = False
    for i in range(0, k + 1):
        if math.ceil(hm / (dc + i * w)) <= math.ceil((hc + (k - i) * a) / dm):
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")