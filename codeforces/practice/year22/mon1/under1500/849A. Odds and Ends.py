n = int(input())
data = list(map(int, input().split()))
if n % 2 == 1 and data[0] % 2 == 1 and data[-1] % 2 == 1:
    print("Yes")
else:
    print("No")