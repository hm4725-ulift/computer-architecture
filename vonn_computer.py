# 프로그램 내장형 컴퓨터: 폰 노이만 구조
#   예) EDVAC


from typing import List
from components.four_bits import *


######################
#       하드웨어       #
######################


def COMPUTER(data: List[WORD]) -> WORD:

    def FETCH(data: List[WORD], pc: int) -> WORD:
        return data[pc]

    def DECODE(instr: WORD):
        op = instr[3]
        addr = instr[0] + 2 * instr[1] + 4 * instr[2] + 8
        return op, addr

    def INSTRUCTION(op: bool, a: WORD, b: WORD) -> WORD:
        s0 = AND4(NOT4((op, op, op, op)), ADD4(a, b))
        s1 = AND4((op, op, op, op), SUB4(a, b))
        return ADD4(s0, s1)

    s = (0, 0, 0, 0)
    for pc in range(8):
        instr = FETCH(data, pc)
        op, addr = DECODE(instr)
        s = INSTRUCTION(op, s, data[addr])
    return s


# Instruction Set Architecture
#   [구조]
#   (a, b, c, d)
#   - a, b, c: address(operand)
#   - d: opcode
#   [제공]
#   1. ADD4: address(0~7), opcode(0)
#     s 레지스터의 값과 data[(a, b, c)+8]의 값을 더해
#     s 레지스터에 저장한다.
#   2. SUB4: address(0~7), opcode(1)
#     s 레지스터의 값에서 data[(a, b, c)+8]의 값을 빼
#     s 레지스터에 저장한다.


######################
#      소프트웨어       #
######################

# 프로그램: RGB 컬러 코드의 합 - 1
#   예시) #FFA3B1: 0 +F +F +A +3 +B +1 -1 => 54

data = [
    # code:
    (1, 0, 0, 0),  # 0x0
    (0, 1, 0, 0),  # 0x1
    (1, 1, 0, 0),  # 0x2
    (0, 0, 1, 0),  # 0x3
    (1, 0, 1, 0),  # 0x4
    (0, 1, 1, 0),  # 0x5
    (1, 1, 1, 1),  # 0x6
    (0, 0, 0, 0),  # 0x7
    # data:
    (0, 0, 0, 0),  # 0x8
    (1, 1, 1, 1),  # 0x9
    (1, 1, 1, 1),  # 0xA
    (0, 1, 0, 1),  # 0xB
    (1, 1, 0, 0),  # 0xC
    (1, 1, 0, 1),  # 0xD
    (1, 0, 0, 0),  # 0xE
    (1, 0, 0, 0),  # 0xE
]

print("실행 결과: ", COMPUTER(data))
