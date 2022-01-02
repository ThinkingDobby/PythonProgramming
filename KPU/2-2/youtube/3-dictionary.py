# 중괄호로 표현
# Hash Map과 동일

dic = {'a': 1, 'b': 2, 'c': 3}  # 코틀린: dic = hashMapOf('a' to 1, 'b' to 2, 'c' to 3)
print(dic['b'])
print(dic.get('e', "empty"))

dic['name'] = 'anonymous'
print(dic)

print(dic.keys())   # 코틀린: dic.keys
print(dic.values()) # 코틀린: dic.values
print(dic.items())  # 각 key-value 쌍을 튜플 형태로 변환한 새로운 리스트

for i in dic.keys():
    print(i)

for k, v in dic.items():
    print(k, end = ' ')
    print(v)

if 'a' in dic:
    print("true")

dic.clear()
print(dic)

dic.update(a = 1, b = 2)
print(dic)
dic.update({'c': 2, 'd': 3})
print(dic)