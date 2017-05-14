"""
Given two binary strings,
return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


def add_binary(a, b):
    s = bin(sum([int(a,2),int(b,2)])).split('b')[1]
    return s
