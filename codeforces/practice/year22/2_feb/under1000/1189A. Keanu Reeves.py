n = int(input())
data = input()
if data.count('1') == data.count('0'):
    print(2)
    print(''.join(data[:-1]), data[-1])
else:
    print(1)
    print(''.join(data))