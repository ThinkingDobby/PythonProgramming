class Calculator:
    def __init__(self): # 예악어 - 생성자
        self.result = 0
    def add(self, num): # self 명시, 인스턴스 -> self
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal2.add(2))

# class Outer(object):
#     def __init__(self, outer_num):
#         self.outer_num = outer_num

#     def create_inner_class(outer_self, inner_arg):       self 인자를 명시함으로써(다른 이름으로 지정 가능) 구분이 가능
#         class Inner(object):                             이 경우 self와 outer_self
#             inner_arg = inner_arg
#             def weird_sum_with_closure_scope(inner_self, num)
#                 return num + outer_self.outer_num + inner_arg
#         return Inner


class Calculator2:
    # first = 0     # 클래스 변수
    # second = 0
    def __init__(self, first, second):
        self.first = first  # 객체 변수 - 객체마다 값이 달라야하는 경우
        self.second = second
    def setdata(self, first, second):   
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def div(self):
        return self.first / self.second

a = Calculator2(2, 3)
print(a.add())


class MorecCalculator(Calculator2): # 상속
    def pow(self):
        return self.first**self.second
    def div(self):
        return 0 if self.second == 0 else self.first / self.second  # 오버라이딩

b = MorecCalculator(3, 0)
print(b.add())
print(b.pow())
print(b.div())


class Test:
    first = 5
    second = 5
    def change(self):
        self.first = 2
    def get_value(self):
        return self.first, self.second

test = Test()
Test.second = 3 # 클래스 변수 자체를 변경할 수 있음
test.change()
print(test.get_value())
print(Test.first)