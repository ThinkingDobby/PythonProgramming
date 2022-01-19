n = int(input())
data = [0] + list(map(int, input().split()))
print(sum([(i - 1) * 2 * 2 * data[i] for i in range(1, n + 1)]))