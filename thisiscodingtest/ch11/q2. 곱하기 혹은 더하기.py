data = list(map(int, input()))
for i in range(1, len(data)):
    if data[i - 1] in (0, 1) or data[i] in (0, 1):
        data[i] = data[i - 1] + data[i]
    else:
        data[i] = data[i - 1] * data[i]

print(data[-1])

"""
02984
"""