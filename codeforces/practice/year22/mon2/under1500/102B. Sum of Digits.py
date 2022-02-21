n = input()

cnt = 0
while len(n) != 1:
    s = 0
    for i in range(len(n)):
        s += int(n[i])  # map과 sum 한 번에 적용해야
    n = str(s)
    cnt += 1

print(cnt)