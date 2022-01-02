import mod  # 모듈 임포트
print(mod.add(2, 3))


import sys  # 외부 모듈 import시 시스템 path에 추가 필요
sys.path.append("C:\\Users\\chiho\\PythonProgramming\\KPU\\2-2\\youtube\\modTest")

from mod2 import print_hello    # 함수만 가져와 사용할 수 있음
print_hello("python")
