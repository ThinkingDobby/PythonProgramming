i = input().split()
n = int(input())
print(sorted(i, key = lambda x: (x[n], x)))
