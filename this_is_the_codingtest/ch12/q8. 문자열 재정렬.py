s = input()

alpha = []
digit = []

for i in s:
    if i.isdigit():
        digit.append(int(i))
    else:
        alpha.append(i)

print(''.join(sorted(alpha)) + str(sum(digit)))

"""
K1KA5CB7
"""