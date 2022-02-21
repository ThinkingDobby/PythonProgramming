n = int(input())
data = list(map(int, input().split()))
if n == 1:
    print("YES" if data[0] == 1 else "NO")
else:
    print("YES" if data.count(0) == 1 else "NO")