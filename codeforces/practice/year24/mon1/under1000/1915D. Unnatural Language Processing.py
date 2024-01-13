import sys

input = sys.stdin.readline

vowels = {'a', 'e'}
consonants = {'b', 'c', 'd'}

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    ans = ""

    i = 0
    while i < n:
        if i + 3 < n - 1 and data[i + 2] in consonants and data[i + 3] in consonants:
            ans += data[i:i + 3] + "."
            i += 3
        else:
            ans += data[i:i + 2] + "."
            i += 2

    print(ans)
