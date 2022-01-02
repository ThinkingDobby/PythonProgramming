add = lambda a, b: a + b
print(add(1, 2))

my_list = [lambda a, b: a + b, lambda a, b: a - b]  # 코틀린: val myList = listOf({a:Int, b: Int -> a + b}, {a: Int, b: Int -> a - b})
print(my_list[0](1, 2))
print(my_list[1](4, 3))


lambda x, y: (x + y, x - y) # 람다식은 튜플로 리턴 시 괄호 필요
# 함수는 return x, y로 괄호 없이 가능