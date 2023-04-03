import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    evens = [i for i in data if i % 2 == 0]
    print("YES" if sum(data) - sum(evens) < sum(evens) else "NO")