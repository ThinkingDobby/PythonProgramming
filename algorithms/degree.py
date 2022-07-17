import math

# 파이썬 삼각함수의 인자, 반환값은 기본적으로 라디안 값

# radian -> degree
# math.radians(deg)
def rad_to_deg(r):
    return (r * 180) / math.pi


# degree -> radian
# math.degrees(rad)
def deg_to_rad(d):
    return (d * math.pi) / 180


# 원점-좌표 간 각도 계산 - 라디안 값
x = 2
y = 2
rad = math.atan2(y, x)
print(rad)
print(rad_to_deg(rad))

# math.sin, math.cos 인자는 라디안 값
s = math.sin(rad)
c = math.cos(rad)
print(s, c)


# 원점 기준 거리 l, 각도(라디안) d인 점의 좌표:
# (l * math.cos(d), l * math.sin(d))
# 이 경우 d > 360 또는 d < 0 이어도 상관 없음
