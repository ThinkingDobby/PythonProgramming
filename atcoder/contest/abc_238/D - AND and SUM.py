# 참조한 코드

for _ in range(int(input())):
    a, s = map(int, input().split())
    if s - a < 0:
        print("No")
    elif (s - a) & a == a:
        print("Yes")
    else:
        print("No")

# x + y = (x & y) + (x | y),
# s = a + (x | y),
# s - a = (x | y)
# 이 때, (x | y) & (x & y) != (x & y)
# 즉, (s - a) & a != a 이면 조건을 만족하는 x, y가 없는 것
# (x & y가 0이면 x | y도 0이고 1이면 x | y도 1이기 때문)
