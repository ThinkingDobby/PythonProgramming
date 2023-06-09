import numpy as np

def f(x):
    return -0.0056*x**3 + 0.0134*x**2 + 0.5190*x + 4.5333

a = 1
b = 10
n = 9
h = (b - a) / n

x = np.linspace(a, b, n + 1)
y = f(x)

# Apply Simpson's 1/3 rule
integral = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))

print("The approximate value of the integral is", integral)
