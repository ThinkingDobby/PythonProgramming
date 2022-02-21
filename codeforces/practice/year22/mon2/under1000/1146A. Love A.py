n = input()
cnt = n.count('a')
print(len(n) - max(0, len(n) - (cnt * 2 - 1)))