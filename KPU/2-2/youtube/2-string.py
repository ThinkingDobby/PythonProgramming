a = ' ' # 내부에 " 사용 가능
b = " " # 내부에 " 사용 가능
c = """ """ # 여러 줄 문자열


d = "Python"
e = " is fun"
print(d + e, end = ' ') # 개행 없애기
print(d + e)    # 자동 개행
print(d * 10)
print(d[0])
print(d[-1])    # 음수 이용한 역방향 탐색 가능

# slice: [이상:미만:간격]
f = "12345678"
print(f[2:7:2])
e = "1234321"
print(e == e[::-1]) # 간격에 음수 넣어 팰린드롬 확인도 가능