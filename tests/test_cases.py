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
START
STOP
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
START
STOP
"""

test_2_assert_1 = {'x': 'INT', 'y': 'INT', 'z': 'INT', 'abc': 'FLOAT', 'b': 'FLOAT', 'c': 'FLOAT', 'ch': 'CHAR',
                   'ch2': 'CHAR', 'ch3': 'CHAR', 't': 'BOOL', 'f': 'BOOL'}
test_2_assert_2 = {'x': 0, 'y': 12, 'z': 36, 'abc': 18.0, 'b': -2.2, 'c': 1.5, 'ch': 'c',
                   'ch2': '', 'ch3': 'd', 't': True, 'f': False}


"""
testcase 3
"""
test_3 = """
VAR x=25+2, y=x%3, z=12*3 AS INT
VAR abc=(1+2.0) * 6, b=-2.2, c=+3/2, d=abc+x AS FLOAT
VAR ch='c', ch2, ch3=ch AS CHAR
VAR t="TRUE", f=t AS BOOL
START
STOP
"""

test_3_assert_1 = {'x': 'INT', 'y': 'INT', 'z': 'INT', 'abc': 'FLOAT', 'b': 'FLOAT', 'c': 'FLOAT', 'd': 'FLOAT',
                   'ch': 'CHAR', 'ch2': 'CHAR', 'ch3': 'CHAR', 't': 'BOOL', 'f': 'BOOL'}
test_3_assert_2 = {'x': 27, 'y': 0, 'z': 36, 'abc': 18.0, 'b': -2.2, 'c': 1.5, 'd': 45.0, 'ch': 'c',
                   'ch2': '', 'ch3': 'c', 't': True, 'f': True}


"""
testcase 4
"""
test_4 = """
* my first program in CFPL
VAR abc, b, c AS INT
VAR x, w_23='w' AS CHAR
VAR t="TRUE" AS BOOL
START
* this is a comment
STOP
"""

test_4_assert_1 = {'abc': 'INT', 'b': 'INT', 'c': 'INT', 'x': 'CHAR', 'w_23': 'CHAR', 't': 'BOOL'}
test_4_assert_2 = {'abc': 0, 'b': 0, 'c': 0, 'x': '', 'w_23': 'w', 't': True}

"""
testcase 5
"""
test_5 = """
* my first program in CFPL
VAR abc, b, c AS INT
VAR x, w_23='w' AS CHAR
VAR t="TRUE" AS BOOL
START
* this is a comment
abc=b=10
w_23='a'
x=w_23
STOP
"""

test_5_assert_1 = {'abc': 'INT', 'b': 'INT', 'c': 'INT', 'x': 'CHAR', 'w_23': 'CHAR', 't': 'BOOL'}
test_5_assert_2 = {'abc': 10, 'b': 10, 'c': 0, 'x': 'a', 'w_23': 'a', 't': True}

"""
testcase 6
"""
test_6 = """
* my first program in CFPL
VAR abc, b, c AS INT
VAR x, w_23='w' AS CHAR
VAR t="TRUE" AS BOOL
START
* this is a comment
abc=b=10
w_23='a'
x=w_23
OUTPUT: abc & "hi" & b & "#" & w_23 & "[#]"
STOP
"""

test_6_assert_1 = {'abc': 'INT', 'b': 'INT', 'c': 'INT', 'x': 'CHAR', 'w_23': 'CHAR', 't': 'BOOL'}
test_6_assert_2 = {'abc': 10, 'b': 10, 'c': 0, 'x': 'a', 'w_23': 'a', 't': True}

"""
testcase 7
"""
test_7 = """
VAR xyz, abc=100 AS INT
START
xyz= ((abc *5)/10 + 10) * -1
* xyz should have the value -60
OUTPUT: "[[]" & xyz & "[]]"
STOP

"""

test_7_assert_1 = {'xyz': 'INT', 'abc': 'INT'}
test_7_assert_2 = {'xyz': -60, 'abc': 100}
