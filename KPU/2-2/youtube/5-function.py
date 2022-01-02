def sum(a, b):
    return a + b
print(sum(3, 5))

def sum_many(*args):    # 여러개의 인자 튜플로 받기
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_many(1, 2, 3, 4))

def print_kwargs(**kwargs): # 여러개의 인자 딕셔너리 형태로 받기
    print(kwargs)
    for k in kwargs.keys():
        if (k == "name"):
            print("name is " + kwargs[k])
print_kwargs(a = 1, name = "2") # 함수 인자 입력하듯 입력 -> key는 str

def sum_and_mul(a, b):
    return a + b, a * b # 여러 값 반환 - 튜플 형태로 반환됨
print(sum_and_mul(3, 5)[0])

def say(a = "Hi"):  # default 값 설정
    print(a)
say()

def div(a, b):
    return a / b
print(div(b = 4, a = 8))