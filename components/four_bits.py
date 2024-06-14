# 4-bit components

from typing import Tuple
from components.one_bit import *

WORD = Tuple[bool, bool, bool, bool]


def AND4(a: WORD, b: WORD) -> WORD:
    return (AND(a[0], b[0]), AND(a[1], b[1]), AND(a[2], b[2]), AND(a[3], b[3]))


def OR4(a: WORD, b: WORD) -> WORD:
    return (OR(a[0], b[0]), OR(a[1], b[1]), OR(a[2], b[2]), OR(a[3], b[3]))


def NOT4(a: WORD) -> WORD:
    return (NOT(a[0]), NOT(a[1]), NOT(a[2]), NOT(a[3]))


def ADD4(a: WORD, b: WORD) -> WORD:
    s0, c1 = HALF_ADDER(a[0], b[0])
    s1, c2 = FULL_ADDER(a[1], b[1], c1)
    s2, c3 = FULL_ADDER(a[2], b[2], c2)
    s3, c4 = FULL_ADDER(a[3], b[3], c3)
    # if c4 != 0:
    #     print("overflow!")
    return (s0, s1, s2, s3)


def TWOS_COMPLEMENT4(a: WORD) -> WORD:
    return ADD4((NOT(a[0]), NOT(a[1]), NOT(a[2]), NOT(a[3])), (1, 0, 0, 0))


def SUB4(a: WORD, b: WORD) -> WORD:
    return ADD4(a, TWOS_COMPLEMENT4(b))
