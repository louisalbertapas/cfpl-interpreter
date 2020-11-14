"""
File:           Parser.py
Description:    A Parser class takes the tokens and transforms it to nodes in an Abstract Syntax Tree (AST)
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""
from constants.reserved_keywords import *
from cfpl.AbstractSyntaxTree import *


class Parser(object):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        # set current token to the first token taken from the input
        self.current_token = self.tokenizer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def consume(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "consume" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.tokenizer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INT_CONST | LEFT_PAREN expr RIGHT_PAREN"""
        token = self.current_token
        if token.type == INT_CONST:
            self.consume(INT_CONST)
            return Num(token)
        elif token.type == LEFT_PAREN:
            self.consume(LEFT_PAREN)
            node = self.expr()
            self.consume(RIGHT_PAREN)
            return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.consume(MUL)
            elif token.type == DIV:
                self.consume(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INT_CONST | LEFT_PAREN expr RIGHT_PAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.consume(PLUS)
            elif token.type == MINUS:
                self.consume(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()
