# 패키지
# 모듈을 묶은 것 (모듈 + 디렉터리)

from game.sound.echo import echo_test
echo_test()

from game.graphic.render import render_test as r
r()

from game.graphic import *  # 패키지 __init__.py 파일에 *로 import할 파일 명시 필요
color.color_test()          # __all__ = ['color', 'render']