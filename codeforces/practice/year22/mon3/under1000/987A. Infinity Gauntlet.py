memo = {"Power": "purple", "Time": "green", "Space": "blue", "Soul": "orange", "Reality": "red", "Mind": "yellow"}

n = int(input())
data = [input() for _ in range(n)]

ans = []
for i in memo.keys():
    if memo[i] not in set(data):
        ans.append(i)

print(len(ans))
print("\n".join(ans))