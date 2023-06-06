import numpy as np

def f(x):
    return x * np.cos(x)

a = 0
b = np.pi/2
h = np.pi/4

# We need to have a multiple of 3 segments
n = int((b - a) / h)
while n % 3 != 0:
    n += 1
h = (b - a) / n

x = np.linspace(a, b, n + 1)
y = f(x)

# Apply Simpson's 3/8 rule
integral = 3 * h / 8 * (y[0] + y[-1] + 3 * np.sum(y[1:-1:3]) + 3 * np.sum(y[2:-1:3]) + 2 * np.sum(y[3:-1:3]))

print("The approximate value of the integral is", integral)

