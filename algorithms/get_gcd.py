# import math
# math.gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# LCM(최소공배수) = a * b / gcd

