n = int(input())
data = list(input())
ans = min(data.count('L'), data.count('R')) * 2 + min(data.count('U'), data.count('D')) * 2
print(ans)
