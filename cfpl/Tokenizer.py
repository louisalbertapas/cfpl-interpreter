"""
File:           Tokenizer.py
Description:    A Tokenizer class breaks down the code into tokens during lexical analysis
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""

from cfpl import Token
from constants.reserved_keywords import *


class Tokenizer(object):
    def __init__(self, text):
        self.lines = text.split("\n")
        if len(self.lines) == 0:
            self.error()
        self.line = -1
        self.text = ""
        self.pos = 0
        self.current_char = ""
        self.next_line()

    def error(self):
        raise Exception('Invalid character')

    def next_line(self):
        self.line += 1
        if self.line < len(self.lines):
            line = self.lines[self.line].strip()
            if len(line) == 0 or line[0] == '*':  # comment
                return self.next_line()
            else:
                self.pos = 0
                self.text = ' ' + self.lines[self.line]  # MUST add space before or after
                self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.next_line()  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def peek(self, direction=1, step=1):  # 1 - front, -1 back
        if direction == 1:
            peek_pos = self.pos + step
            if peek_pos > len(self.text) - 1:
                return None
            else:
                return self.text[peek_pos]
        elif direction == -1:
            back_pos = self.pos - step
            if back_pos > len(self.text) - 1:
                return None
            else:
                return self.text[back_pos]
        else:
            raise Exception('wrong peek parameter')

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        """Return a (multidigit) integer or float consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

            token = Token(FLOAT_CONST, float(result))
        else:
            token = Token(INT_CONST, int(result))

        return token

    def char(self):
        if self.current_char == '\'':
            char = ''
        else:
            char = self.current_char
            self.advance()
        self.advance()
        return Token('CHAR_CONST', char)

    def string_or_bool(self):
        result = ''
        while self.current_char is not None:
            if self.current_char == '[' and self.peek(1, 2) == ']':  # first
                self.advance()
                continue
            if self.peek(-1) == '[' and self.peek(1) == ']':  # middle
                result += self.current_char
                self.advance()
                continue
            if self.current_char == ']' and self.peek(-1, 2) == '[':  # last
                self.advance()
                continue
            if self.current_char == '"':  # reached the end of string
                self.advance()
                break

            result += self.current_char if self.current_char != '#' else "\n"
            self.advance()

        if result in ['TRUE', 'FALSE']:
            return Token(BOOL_CONST, result)
        else:
            return Token(STRING_CONST, result)

    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()

        token = RESERVED_KEYWORDS.get(result, Token(ID, result))
        return token

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == '\'':
                self.advance()
                return self.char()

            if self.current_char == '"':
                self.advance()
                return self.string_or_bool()

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '%':
                self.advance()
                return Token(MOD, '%')

            if self.current_char == '(':
                self.advance()
                return Token(LEFT_PAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RIGHT_PAREN, ')')

            if self.current_char.isalpha() or self.current_char == '_':
                return self._id()

            if self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')

            if self.current_char == '&':
                self.advance()
                return Token(AMPERSAND, '&')

            if self.current_char == ':':
                self.advance()
                return Token(COLON, ':')

            if self.current_char == '<' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(LESSER_EQUAL, '<=')

            if self.current_char == '>' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(GREATER_EQUAL, '>=')

            if self.current_char == '=' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(EQUAL, '==')

            if self.current_char == '<' and self.peek() == '>':
                self.advance()
                self.advance()
                return Token(NOT_EQUAL, '<>')

            if self.current_char == '<':
                self.advance()
                return Token(LESSER_THAN, '<')

            if self.current_char == '>':
                self.advance()
                return Token(GREATER_THAN, '>')

            if self.current_char == '=':
                self.advance()
                return Token(ASSIGN, '=')

            self.error()

        return Token(EOF, None)
