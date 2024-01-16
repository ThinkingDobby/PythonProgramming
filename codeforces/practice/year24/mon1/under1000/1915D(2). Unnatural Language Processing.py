import sys

input = sys.stdin.readline

vowels = {'a', 'e'}
consonants = {'b', 'c', 'd'}

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    i = n - 1
    ans = []
    while i >= 0:
        if data[i] in consonants:
            ans.append(data[i - 2:i + 1])
            i -= 3
        else:
            ans.append(data[i - 1:i + 1])
            i -= 2

    print('.'.join(reversed(ans)))