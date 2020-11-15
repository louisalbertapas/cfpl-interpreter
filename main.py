"""
File:           main.py
Description:    Driver function to run the CFPL interpreter
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""


from constants.reserved_keywords import *
from cfpl.Token import Token
from cfpl.Tokenizer import Tokenizer
from cfpl.Parser import Parser
from cfpl.Interpreter import Interpreter
from tests.test_cases import *
from constants.debug import *

text = test_2
tokenizer = Tokenizer(text)
if print_token:
    while True:
        token = tokenizer.get_next_token()
        print(token)
        if token.__str__() == "Token(EOF, None)":
            break

tokenizer = Tokenizer(text)
# convert tokens into nodes and store in an Abstract Syntax Tree fashion
parser = Parser(tokenizer)

# interprets the Abstract Syntax Tree using visitor pattern
interpreter = Interpreter(parser)
result = interpreter.interpret()
if test_2_assert:
    assert (interpreter.SYMBOL_TABLE_TYPE == test_2_assert_1)
    assert (interpreter.SYMBOL_TABLE_VALUE == test_2_assert_2)
if debug:
    print("SYMBOL_TABLE_TYPE: " + interpreter.SYMBOL_TABLE_TYPE.__str__())
    print("SYMBOL_TABLE_VALUE: " + interpreter.SYMBOL_TABLE_VALUE.__str__())
