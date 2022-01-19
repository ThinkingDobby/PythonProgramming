n = int(input())
data = [int(input()) for i in range(n)]
print(*sorted(data, reverse=True))