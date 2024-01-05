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
        if data[i] in consonants and i + 1 < n and data[i + 1] in vowels:
            if i + 2 < n and data[i + 2] in consonants:
                ans += data[i:i + 3] + '.'
                i += 2
            else:
                ans += data[i:i + 2] + '.'
                i += 1
        else:
            i += 1

    print(ans)
