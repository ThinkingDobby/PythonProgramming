a = "I eat " + str(3) + " apples."
print(a)
b = "I eat %d apples." % 3
print(b)


num = 10
day = "three"
result = "I ate %d apples. So I was sick for %s days." %(num, day)
print(result)

c = "1234 {} 1234 {}".format("hello", "hi")
print(c)

e = "I ate {num} apples. So I was sick for {day} days.".format(num = 10, day = "three")
print(e)

name = "Python"
tmp = f"My name is {name}"  # 파이썬 3.6 부터 가능
print(tmp)

f = "%.4f" % 3.421343234   # 출력할 소수점 자리 수 결정
print(f)