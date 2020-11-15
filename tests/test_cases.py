"""
Contains test cases.

A test case contains one test code and optional assertion baseline

Format:
test_{N} = "lines of code"

test_{N}_assert_{M} = something to assert
"""


"""
testcase 1
"""
test_1 = """
VAR abc, b, c AS INT
VAR a AS FLOAT
VAR ch1, ch2 AS CHAR
VAR t,f AS BOOL
"""

test_1_assert_1 = {'abc': 'INT', 'b': 'INT', 'c': 'INT', 'a': 'FLOAT', 'ch1': 'CHAR', 'ch2': 'CHAR', 't': 'BOOL', 'f': 'BOOL'}
test_1_assert_2 = {'abc': 0, 'b': 0, 'c': 0, 'a': 0.0, 'ch1': '', 'ch2': '', 't': False, 'f': False}

"""
testcase 2
"""
test_2 = """
VAR x=25%5, y=24/2, z=12*3 AS INT
VAR abc=(1+2.0) * 6, b=-2.2, c=+3/2 AS FLOAT
VAR ch='c', ch2, ch3='d' AS CHAR
VAR t="TRUE", f AS BOOL
"""

test_2_assert_1 = {'x': 'INT', 'y': 'INT', 'z': 'INT', 'abc': 'FLOAT', 'b': 'FLOAT', 'c': 'FLOAT', 'ch': 'CHAR',
                   'ch2': 'CHAR', 'ch3': 'CHAR', 't': 'BOOL', 'f': 'BOOL'}
test_2_assert_2 = {'x': 0, 'y': 12, 'z': 36, 'abc': 18.0, 'b': -2.2, 'c': 1.5, 'ch': 'c',
                   'ch2': '', 'ch3': 'd', 't': True, 'f': False}