data = ['A'] + list(input()) + ['A']
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
mv = -1
prev = -1
for i in range(len(data)):
    if data[i] in vowels:
        mv = max(mv, i - prev)
        prev = i

print(mv)