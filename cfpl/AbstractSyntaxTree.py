"""
File:           AbstractSyntaxTree.py
Description:    An Abstract Syntax Tree (AST) implementation to convert tokens into nodes
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""


class AST(object):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
