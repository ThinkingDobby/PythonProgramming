a = 1
def var_test(a):    # 지역 변수 a
    a = a + 1

var_test(a)
print(a)


def var_test_global():
    global a    # 전역 변수 a 가져옴
    a = a + 1

var_test_global()
print(a)