from constants.reserved_keywords import *
from cfpl.Token import Token
from cfpl.Tokenizer import Tokenizer

# Sample test for tokenizing basic arithmetic expression
tokenizer = Tokenizer('4 + 2 * 1 / (1 + 20)')
while True:
    token = tokenizer.get_next_token()
    print(token)
    if token.__str__() == "Token(EOF, None)":
        break
