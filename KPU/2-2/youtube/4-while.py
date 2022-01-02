i = 0
while i < 10:
    print("%d" % i, end = ' ')
    i += 1  # ++ 표현(증감연산자) 사용 불가
print()

cnt = 10
while True:
    cnt -= 1
    print("{cnt}".format(cnt=cnt), end = ' ')
    if not cnt:
        break
print()

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(f"{i}", end = ' ')
print()
