from constants.reserved_keywords import *
from cfpl.Token import Token
from cfpl.Tokenizer import Tokenizer
from cfpl.Parser import Parser
from cfpl.Interpreter import Interpreter

# Sample test for tokenizing basic arithmetic expression
tokenizer = Tokenizer('4 - 2 * 1 + (1 + 20)')
"""
while True:
    token = tokenizer.get_next_token()
    print(token)
    if token.__str__() == "Token(EOF, None)":
        break
"""

# convert tokens into nodes and store in an Abstract Syntax Tree fashion
parser = Parser(tokenizer)

# interprets the Abstract Syntax Tree using visitor pattern
interpreter = Interpreter(parser)
result = interpreter.interpret()
print(result)
