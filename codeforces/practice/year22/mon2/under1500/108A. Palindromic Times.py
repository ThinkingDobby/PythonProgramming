h, m = map(int, input().split(':'))
tot = h * 60 + m + 1

if tot in range(0, 351):
    tmp = ((tot + 70 - 1) // 70) * 70
elif tot in range(351, 602):
    tmp = 601
elif tot in range(602, 952):
    tmp = ((tot - 601 + 70 - 1) // 70) * 70 + 601
elif tot in range(952, 1203):
    tmp = 1202
elif tot in range(1203, 1413):
    tmp = ((tot - 1202 + 70 - 1) // 70) * 70 + 1202
else:
    tmp = 0

nh = tmp // 60
nm = tmp % 60

print("%02d:%02d" % (nh, nm))
