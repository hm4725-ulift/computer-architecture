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
    s0, c1 = XOR(data[0][0], data[1][0]), AND(data[0][0], data[1][0])
    s1, c2 = FULL_ADDER(data[0][1], data[1][1], c1)
    s2, c3 = FULL_ADDER(data[0][2], data[1][2], c2)
    s3, _ = FULL_ADDER(data[0][3], data[1][3], c3)
    s0, c1 = XOR(s0, data[2][0]), AND(s0, data[2][0])
    s1, c2 = FULL_ADDER(s1, data[2][1], c1)
    s2, c3 = FULL_ADDER(s2, data[2][2], c2)
    s3, _ = FULL_ADDER(s3, data[2][3], c3)
    s0, c1 = XOR(s0, data[3][0]), AND(s0, data[3][0])
    s1, c2 = FULL_ADDER(s1, data[3][1], c1)
    s2, c3 = FULL_ADDER(s2, data[3][2], c2)
    s3, _ = FULL_ADDER(s3, data[3][3], c3)
    s0, c1 = XOR(s0, data[4][0]), AND(s0, data[4][0])
    s1, c2 = FULL_ADDER(s1, data[4][1], c1)
    s2, c3 = FULL_ADDER(s2, data[4][2], c2)
    s3, _ = FULL_ADDER(s3, data[4][3], c3)
    s0, c1 = XOR(s0, data[5][0]), AND(s0, data[5][0])
    s1, c2 = FULL_ADDER(s1, data[5][1], c1)
    s2, c3 = FULL_ADDER(s2, data[5][2], c2)
    s3, _ = FULL_ADDER(s3, data[5][3], c3)
    s0, c1 = XOR(s0, 1), AND(s0, 1)
    s1, c2 = FULL_ADDER(s1, 1, c1)
    s2, c3 = FULL_ADDER(s2, 1, c2)
    s3, _ = FULL_ADDER(s3, 1, c3)
    return (s0, s1, s2, s3)


data = [
    (1, 1, 1, 1),
    (1, 1, 1, 1),
    (0, 1, 0, 1),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 0, 0, 0),
]

print("실행 결과: ", COMPUTER(data))
