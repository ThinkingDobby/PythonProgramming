# 주석은 코틀린에서 동일 기능을 수행하는 함수

a = "hobby"
print(a.count("b")) # a.count {it == "b"}
print(a.find("y"))  # a.indexOf('y')

b = ",".join("abcd") # b.toCharArray().joinToString(",")
print(b)

c = ",".join(["a", "b", "c", "d"])  # 리스트에 join
print(c)

print(a.upper())    # a.toUpperCase()

d = "   HI   "
print(d.strip())    # d.trim()

e = "Life is too short"
print(e.replace("short", "long"))

f = "a b c d"
print(f.split(" "))
