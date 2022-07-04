data = ['a'] + list(input()) + ['a']
zero = 0
one = 0
for i in range(1, len(data)):
    if data[i] != data[i - 1] and data[i] == '1':
        one += 1
    elif data[i] != data[i - 1] and data[i] == '0':
        zero += 1

print(min(one, zero))