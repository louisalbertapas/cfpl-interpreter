from constants.tokens import *
from cfpl.Token import Token

RESERVED_KEYWORDS = {
    'START': Token(START, START),
    'STOP': Token(STOP, STOP),
    'VAR': Token(VAR, VAR),
    'AS': Token(AS, AS),
    'INT': Token(INT, INT),
    'CHAR': Token(CHAR, CHAR),
    'BOOL': Token(BOOL, BOOL),
    'FLOAT': Token(FLOAT, FLOAT),
    'INPUT': Token(INPUT, INPUT),
    'OUTPUT': Token(OUTPUT, OUTPUT),
    'AND': Token(AND, AND),
    'OR': Token(OR, OR),
    'NOT': Token(NOT, NOT),
    'IF': Token(IF, IF),
    'ELSE': Token(ELSE, ELSE),
    'WHILE': Token(WHILE, WHILE)
}
