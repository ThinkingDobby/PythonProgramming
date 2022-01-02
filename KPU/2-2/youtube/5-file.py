#
# Write
#

f = open("5-file_test.txt", 'w')   # r: Read, w: Write, a: Add
f.close()

f = open("5-file_test.txt", 'w', encoding = "UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


#
# Read
#

f = open("5-file_test.txt", 'r', encoding = "UTF-8")
line = f.readline() # 한 줄 읽어옴
print(line)
f.close()

f = open("5-file_test.txt", 'r', encoding = "UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line, end = '')
f.close()

f = open("5-file_test.txt", 'r', encoding = "UTF-8")
lines = f.readlines()   # 모든 데이터 리스트 형태로 읽어옴(행 단위)
print(lines)
f.close()

f = open("5-file_test.txt", 'r', encoding = "UTF-8")
lines = f.read()    # 모든 데이터 그대로 읽어옴
print(lines)
f.close()


#
# Add
#

f = open("5-file_test.txt", 'a', encoding = "UTF-8")
f.write("add\n")
f.close()

f = open("5-file_test.txt", 'r', encoding = "UTF-8")
print(f.read())
f.close()


#
#
#

with open("5-file_test.txt", "r", encoding = "UTF-8") as f: # with 사용 시 별도 close 필요x
    print(f.read())