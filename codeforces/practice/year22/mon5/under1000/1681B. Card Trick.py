import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    memo = list(map(int, input().split()))
    print(data[sum(memo) % n])
