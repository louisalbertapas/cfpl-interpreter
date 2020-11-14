"""
File:           tokens.py
Description:    Contains all the type of tokens
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""

# Data types tokens
INT = 'INT'
CHAR = 'CHAR'
BOOL = 'BOOL'
FLOAT = 'FLOAT'

# Operator tokens
# Arithmetic operators
PLUS = 'PLUS'  # could be a unary operator + or binary operator addition
MINUS = 'MINUS'  # could be a unary operator - or binary operator subtraction
MUL = 'MUL'
DIV = 'DIV'
MOD = 'MOD'
GREATER_THAN = 'GREATER_THAN'
LESSER_THAN = 'LESSER_THAN'
GREATER_EQUAL = 'GREATER_EQUAL'
LESSER_EQUAL = 'LESSER_EQUAL'
EQUAL = 'EQUAL'
NOT_EQUAL = 'NOT_EQUAL'
LEFT_PAREN = 'LEFT_PAREN'
RIGHT_PAREN = 'RIGHT_PAREN'

# Logical operators
AND = 'AND'
OR = 'OR'
NOT = 'NOT'

# Control structure operators
IF = 'IF'
ELSE = 'ELSE'
WHILE = 'WHILE'

# Other reserved words tokens
START = 'START'
STOP = 'STOP'
VAR = 'VAR'
AS = 'AS'
INPUT = 'INPUT'
OUTPUT = 'OUTPUT'

# Symbols tokens
ID = 'ID'
ASSIGN = 'ASSIGN'
COMMA = 'COMMA'
SHARP = 'SHARP'
AMPERSAND = 'AMPERSAND'
COLON = 'COLON'
LEFT_SQUARE_BRACE = 'LEFT_SQUARE_BRACE'
RIGHT_SQUARE_BRACE = 'RIGHT_SQUARE_BRACE'
EOF = 'EOF'

# Constant value tokens
INT_CONST = 'INT_CONST'
CHAR_CONST = 'CHAR_CONST'
BOOL_CONST = 'BOOL_CONST'
FLOAT_CONST = 'FLOAT_CONST'
STRING_CONST = 'STRING_CONST'
