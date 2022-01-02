# try:
# except Exception as e:
# else:
# finally:

try:
    4 / 0
except ZeroDivisionError as e:  # 여러 예외 조건 설정 가능
    print(e)
except IndexError:
    pass
else:   # 코틀린에서는 이 부분을 try블록에 이어서 작성
    print("success")
finally:
    print("finally")

print("test")


class Bird:
    def fly(self):
        raise NotImplementedError   # 의도적 예외 던지기

class Eagle(Bird):
    def fly(self):
        print("fast")

eagle = Eagle()
try:
    eagle.fly()
except NotImplementedError:
    print("err")
finally:
    print("test")