import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, k = map(int, input().split())
data = sorted(enumerate(map(int, input().split())), key=lambda x: x[1], reverse=True)
print(data[k - 1][1])
print(*[i[0] + 1 for i in data[:k]])