test_list = ["one", "two", "three"]
for i in test_list:
    print(f"{i}", end = ' ')
print()

a = [(1, 2), (3, 4), (5, 6)]
for (first, second) in a:
    print("%d" % (first + second), end = ' ')
print()

for i in range(1, 10):
    print("%d"%i, end = ' ')
print()

for i in range(2, 10):
    for j in range(1, 10):
        print("%3d" %(i * j), end = ' ')
    print()

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0] # 리스트 내포
print(result)