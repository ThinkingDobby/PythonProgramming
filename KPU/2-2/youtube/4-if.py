money = True
if 1:
    print("get Taxi")   # 들여쓰기 틀리면 오류 발생
else:
    print("walk")

a = 1
b = 2
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# and   코틀린 &&
# or    코틀린 ||
# not

card = True
if money and card:
    print("get Taxi")
else:
    print("walk")

if 1 in [1, 2, 3]:
    pass    # 아무 것도 안쓸 수 x
else:
    print("no")

age = 35
if age > 40:
    print("high")
elif age > 30:  # else if
    print("medium")
else:
    print("low")


message = "high" if age > 30 else "low" # 조건부 표현식 - 참일 때 값 먼저 명시
# 코틀린: val message = if (age > 30) "high" else "low"
# 자바스크립트: const message = age > 30 ? "high" : "low"; - 삼항연산자
print(message)
