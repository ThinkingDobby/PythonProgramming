# 내장 함수
# 바로 사용 가능

print(abs(-3))
print(all([1, 2, 3, 0]))
print(any([1, 2, 3, 0]))
print(chr(48))

def positive(x):
    return x > 0
a = list(filter(positive, [1, 2, -3, 4, -5]))   # filter
print(a)

print(len("asdf"))

a = list(map(lambda a: a * 2, [1, 2, 3, 4]))    # map
print(a)