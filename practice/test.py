import math

a = math.radians(47)
print(a)

b = math.degrees(a)
print(b)

# radian -> degree
def rad_to_deg(r):
    return (r * 180) / math.pi

# degree -> radian
def deg_to_rad(d):
    return (d * math.pi) / 180

a = deg_to_rad(47)
print(a)
b = rad_to_deg(a)
print(b)