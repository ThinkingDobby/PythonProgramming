n = int(input())
data = input()
print(n - len(set(data)) if n <= 26 else -1)