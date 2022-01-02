data = """
park 800905-1094118
kim 700905-1059119
"""

import re   # 정규표현식 지원하는 모델
p = re.compile("([0-9]{6})[-]([0-9]{7})") # 패턴 객체 생성
print(p.sub("\g<1>-******", data))

# [abc] : a, b, c 중 하나와 일치
# . : 한 문자와 일치
# * : 앞 문자가 0~여러번 반복
# + : 앞 문자가 1~여러번 반복
# {2, 5} : 앞 문자가 2번 또는 5번 반복
# ? : 앞 문자가 없거나 한 개 {0, 1}과 동일

p = re.compile("[a-z]+")
m = p.match("3 python") # 일치하는지
print(m)

m = p.search("3 python")    # 탐색
print(m)

m = p.findall("life is too short")  # 일치하는 String들을 list로 반환
print(m)

m = p.finditer("life is too short") # 일치하는 String들을 iterator 형식으로 반환
print(m)
for i in m:
    print(i)

# match 객체 - 매칭된 내용
m = p.match("python")
print(m.group())    # 매치된 문자열
print(m.start())    # start 인덱스
print(m.end())  # end 인덱스
print(m.span()) # start, end 튜플 형태


# 컴파일 옵션
# DOTALL, S
p = re.compile("a.b", re.DOTALL)    # .이 개행문자도 인식
m = p.match("a\nb")
print(m)

# IGNORECASE, I
p = re.compile("[a-z]", re.I)
print(p.match("PYTHON"))

# MULTILINE, M
p = re.compile("^python\s\w+", re.M)    # ^ 기준을 각 라인으로
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))

# VERBOSE, X
charref = re.compile(r"""
&[#]
(
    0[0-7]+
    | [0-9]+
    | x[0-9a-fA-F]+
)
;
""", re.VERBOSE)    # regex 여러 줄에 걸쳐 작성 가능


p = re.compile("\\\\section") # 백슬래시는 두개 사용 또는
p = re.compile(r"\\section")    # raw 스트링 표시
print("here")
m = p.match("\\section")
print(m)


# 메타문자

p = re.compile("Crow|Servo")    # or
m = p.match("CrowHello")
print(m)

print(re.search("^Life", "Life is too short"))  # re.search로 한 번에 regex설정, 탐색 가능

print(re.search("short$", "Life is too short"))

print(re.search(r"\bclass\b", "no class at all"))   # <\bclass\b> 자체를 탐색 - raw string


# 그루핑
p = re.compile(r"(ABC)\1") #  -> 첫번째 그룹과 일치하는 항목 의미
m = p.match("ABCABCABC")
print(m)
print(m.group(1))
# ?P<name>을 그룹 안에 넣어 그룸 이름 부여 가능
# (?P=name)으로 regex 명시 중 호출 가능
p = re.compile("(?P<name>ABC)(?P=name)")
m = p.match("ABCABC")
print(m.group())


# 전방탐색: 긍정형(?=)
p = re.compile(".+(?=:)")   # until 설정
m = p.search("http://google.com")
print(m.group())

# 전방탐색: 부정형(?!)
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)


# 문자열 바꾸기: sub
p = re.compile("(blue|white|red)")
print(p.sub("color", "blue socks and red shoes"))

# Greedy, Non-Greedy
s = "<html><head><title>Title</title>"
print(re.match("<.*>", s).group()) # Greedy
print(re.match("<.*?>", s).group()) # Non-Greedy