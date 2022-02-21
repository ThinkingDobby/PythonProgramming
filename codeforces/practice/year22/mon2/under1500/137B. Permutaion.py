n = int(input())
data = list(map(int, input().split()))
print(n - len(set([i for i in data if i <= n])))