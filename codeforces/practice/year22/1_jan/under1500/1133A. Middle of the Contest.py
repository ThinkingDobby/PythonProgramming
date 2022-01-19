h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

tmp1 = h1 * 60 + m1
tmp2 = h2 * 60 + m2

total = (tmp2 - tmp1) // 2 + tmp1
print("%02d:%02d" % (total // 60, total % 60))