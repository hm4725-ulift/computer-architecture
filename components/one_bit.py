# 1-bit components

from typing import Tuple


def AND(a: bool, b: bool) -> bool:
    return a and b


def OR(a: bool, b: bool) -> bool:
    return a or b


def XOR(a: bool, b: bool) -> bool:
    return a ^ b


def NOT(a: bool) -> bool:
    return not a


def HALF_ADDER(a: bool, b: bool) -> Tuple[bool, bool]:
    return (XOR(a, b), AND(a, b))


def FULL_ADDER(a: bool, b: bool, cin: bool) -> Tuple[bool, bool]:
    s0, c0 = HALF_ADDER(a, b)
    s, c1 = HALF_ADDER(s0, cin)
    c = OR(c0, c1)
    return (s, c)
