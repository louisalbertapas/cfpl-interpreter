"""
File:           Interpreter.py
Description:    An Interpreter class that reads through the Abstract Syntax Tree using visitor pattern
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""
from constants.reserved_keywords import *


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return self.visit(node.expr) * 1
        elif op == MINUS:
            return self.visit(node.expr) * -1

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
