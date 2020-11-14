from constants.reserved_keywords import *
from cfpl.Token import Token
from cfpl.Tokenizer import Tokenizer
from cfpl.Parser import Parser
from cfpl.Interpreter import Interpreter

# debug mode
debug = 1

# Sample test for tokenizing basic arithmetic expression
text = """
* this is a comment
VAR abc, b, c AS INT
VAR x, w_23='w' AS CHAR
VAR t="TRUE" AS BOOL
START
abc=b=10
w_23='a'
OUTPUT: abc & "hi" & b & "#" & w_23 & "[#]"
IF (abc > 2)
START
OUTPUT: "abc is greater than 2"
STOP
ELSE
START
OUTPUT: "abc is less than 2"
STOP
WHILE (b <= 20)
START
OUTPUT: b
b = b + 1
STOP
STOP

"""
tokenizer = Tokenizer(text)
if debug:
    while True:
        token = tokenizer.get_next_token()
        print(token)
        if token.__str__() == "Token(EOF, None)":
            break
else:
    # convert tokens into nodes and store in an Abstract Syntax Tree fashion
    parser = Parser(tokenizer)

    # interprets the Abstract Syntax Tree using visitor pattern
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    print(result)
