# 1
def is_odd(num):
    return num % 2 == 1
if is_odd(3): print("odd")
else: print("even")

# 2
def calc_avg(*args):
    return sum(args) / len(args)
print(calc_avg(1, 2, 3, 4, 5))

# 3
#input1 = input("첫번째 숫자를 입력하세요:")
#input2 = input("두번째 숫자를 입력하세요:")

#total = int(input1) + int(input2)
#print("두 수의 합은 %s 입니다" % total)

# 4
# 3

# 5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# 6
with open("test.txt", 'a', encoding = "UTF-8") as f:
    text = input("input: ")
    f.write("\n" + text)
with open("test.txt", 'r', encoding = "UTF-8") as f:
    print(f.read())

# 7
with open("test.txt", 'r', encoding = "UTF-8") as f:
    tmp = f.read().replace("java", "python")
with open("test.txt", 'w', encoding = "UTF-8") as f:
    f.write(tmp)
with open("test.txt", 'r', encoding = "UTF-8") as f:
    print(f.read())