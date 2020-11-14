from constants.tokens import *
from cfpl.Token import Token

RESERVED_KEYWORDS = {
    'START': Token(START, START),
    'STOP': Token(STOP, STOP),
    'VAR': Token(VAR, VAR),
    'AS': Token(AS, AS),
    'OUTPUT': Token(OUTPUT, OUTPUT),
    'INT': Token(INT, INT),
    'CHAR': Token(CHAR, CHAR),
    'BOOL': Token(BOOL, BOOL),
    'FLOAT': Token(FLOAT, FLOAT),
    'AND': Token(AND, AND),
    'OR': Token(OR, OR),
    'NOT': Token(NOT, NOT),
}
