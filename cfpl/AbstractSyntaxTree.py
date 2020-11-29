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
        self.name = "bin_op"
        self.left = left
        self.token = self.op = op
        self.right = right
        self.value = None


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.name = "unary_op"
        self.token = self.op = op
        self.expr = expr


class NoOp(AST):
    def __init__(self):
        self.name = "no_op"


class Num(AST):
    def __init__(self, token):
        self.name = "num"
        self.token = token
        self.value = token.value


class Char(AST):
    def __init__(self, token):
        self.name = "char"
        self.token = token
        self.value = token.value


class Bool(AST):
    def __init__(self, token):
        self.name = "bool"
        self.token = token
        self.value = token.value


class String(AST):
    def __init__(self, token):
        self.name = "string"
        self.token = token
        self.value = token.value


class ProgramStart(AST):
    """
    ProgramStart node indicates the start of the program
    """
    def __init__(self, declarations, compound_statements):
        self.name = "program_start"
        self.declarations = declarations
        self.compound_statements = compound_statements


class VariableId(AST):
    """
    VariableId node is mapped with the ID token
    """
    def __init__(self, token):
        self.name = "variable_id"
        self.token = token
        self.value = token.value
        self.default_value = None


class VariableType(AST):
    """
    VariableType node is mapped with either of the following tokens:
    INT | FLOAT | CHAR | BOOL
    """
    def __init__(self, token):
        self.name = "variable_type"
        self.token = token
        self.value = token.value


class VariableDeclaration(AST):
    """
    VariableDeclaration node takes the VariableId and VariableType
    """
    def __init__(self, var_id_node, var_type_node):
        self.name = "variable_declaration"
        self.var_id_node = var_id_node
        self.var_type_node = var_type_node


class CompoundStatements(AST):
    """
    CompoundStatement node takes all kind of statements node inside a START STOP block
    """
    def __init__(self):
        self.name = "compound_statements"
        self.children = []


class Assign(AST):
    """
    Assign takes a variable and an expression
    """
    def __init__(self, left, op, right):
        self.name = "assign"
        self.left = left
        self.token = self.op = op
        self.right = right


class Output(AST):
    """
    Outputs an expression
    """
    def __init__(self, token):
        self.name = "output"
        self.token = token
        self.value = token.value


class IfElse(AST):
    """
    IfElse contains the if block and the optional else block
    """
    def __init__(self, if_token, expr, else_token=None):
        self.name = "if_else"
        self.token = if_token
        self.value = if_token.value
        self.expr = expr
        self.else_token = else_token


class While(AST):
    """
    While node executes a compound statement until the boolean expression is false
    """
    def __init__(self, token, expr):
        self.name = "while"
        self.token = token
        self.value = token.value
        self.expr = expr
