a = 'Life is too short, You need Python'
print(a[28:])
print(a[-6:])


def calc(a, b):
    return a // b, a % b
ans = calc(123456, 123)
print(ans[0])
print(ans[1])


print([i for i in range(1, 101) if '6' in str(i)])


dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={i:j for (i, j) in dict1.items() if j > 2000 }
print(dict2)


i = set("Using dict comprehension and a conditional argument create a dictionary from the current dictionary dict1")
check = {chr(i) for i in range(97, 123)}
print(check - i)