"""
Contains test cases.

A test case contains one test code and optional assertion baseline

Format:
test_{N} = "lines of code"

test_{N}_assert_{M} = something to assert
"""


test_1 = """
VAR abc, b, c AS INT
VAR a AS FLOAT
VAR ch1, ch2 AS CHAR
VAR t,f AS BOOL
"""

test_1_assert_1 = {'abc': 'INT', 'b': 'INT', 'c': 'INT', 'a': 'FLOAT', 'ch1': 'CHAR', 'ch2': 'CHAR', 't': 'BOOL', 'f': 'BOOL'}
test_1_assert_2 = {'abc': 0, 'b': 0, 'c': 0, 'a': 0.0, 'ch1': '', 'ch2': '', 't': False, 'f': False}
