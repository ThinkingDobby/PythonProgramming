n = int(input())
data = list(map(int, input().split()))
b = [(n + 1) - i for i in data]
print(*b)