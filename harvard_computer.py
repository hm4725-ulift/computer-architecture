# 프로그램 내장형 컴퓨터: 하버드 구조
#   예) Harvard Mark I


from typing import List
from components.four_bits import *


######################
#       하드웨어       #
######################


def COMPUTER(code: List[bool], data: List[WORD]) -> WORD:

    def INSTRUCTION(op: bool, a: WORD, b: WORD) -> WORD:
        s0 = AND4(NOT4((op, op, op, op)), ADD4(a, b))
        s1 = AND4((op, op, op, op), SUB4(a, b))
        return ADD4(s0, s1)

    s = (0, 0, 0, 0)
    for pc in range(len(code)):
        s = INSTRUCTION(code[pc], s, data[pc])
    return s


######################
#      소프트웨어       #
######################

# 프로그램: RGB 컬러 코드의 합 - 1
#   예시) #FFA3B1: 0 +F +F +A +3 +B +1 -1 => 54

data = [
    (1, 1, 1, 1),
    (1, 1, 1, 1),
    (0, 1, 0, 1),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 0, 0, 0),
    (1, 0, 0, 0),
]
code = [0, 0, 0, 0, 0, 0, 1]

print("실행 결과: ", COMPUTER(code, data))
