import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

fodd = len([i for i in a if i % 2 == 1])
feven = n - fodd
sodd = len([i for i in b if i % 2 == 1])
seven = m - sodd

print(min(fodd, seven) + min(sodd, feven))