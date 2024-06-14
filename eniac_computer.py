# 초기의 컴퓨터
#   예) ENIAC


from components.four_bits import *
from typing import List


######################
#       하드웨어       #
######################

# 프로그램: RGB 컬러 코드의 합 - 1
#   예시) #FFA3B1: F + F + A + 3 + B + 1 - 1 => 54


def COMPUTER(data: List[WORD]) -> WORD:
    s = ADD4(data[0], data[1])
    s = ADD4(s, data[2])
    s = ADD4(s, data[3])
    s = ADD4(s, data[4])
    s = ADD4(s, data[5])
    s = SUB4(s, (1, 0, 0, 0))
    return s


data = [
    (1, 1, 1, 1),
    (1, 1, 1, 1),
    (0, 1, 0, 1),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 0, 0, 0),
]

print("실행 결과: ", COMPUTER(data))
