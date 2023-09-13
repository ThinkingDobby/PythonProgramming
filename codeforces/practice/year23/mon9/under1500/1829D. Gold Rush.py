import sys
from functools import lru_cache

input = sys.stdin.readline


sys.setrecursionlimit(int(1e5))


@lru_cache
def search(now, target):
    if now == target:
        return True

    if now % 3 == 0:
        if search(now // 3, target) or search(now // 3 * 2, target):
            return True

    return False


for _ in range(int(input())):
    n, m = map(int, input().split())

    print("YES" if search(n, m) else "NO")