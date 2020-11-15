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
        """factor : PLUS factor
                  | MINUS factor
                  | INT_CONST
                  | FLOAT_CONST
                  | LEFT_PAREN expr RIGHT_PAREN
        """
        token = self.current_token
        if token.type == PLUS:
            self.consume(PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == MINUS:
            self.consume(MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == INT_CONST:
            self.consume(INT_CONST)
            return Num(token)
        elif token.type == FLOAT_CONST:
            self.consume(FLOAT_CONST)
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

    def variable_type(self):
        """
        A variable_type is a terminal rule. It indicates the end of a single variable_declaration

        variable_type : INT | FLOAT | CHAR | BOOL
        """
        token = self.current_token
        if self.current_token.type == INT:
            self.consume(INT)
        elif self.current_token.type == FLOAT:
            self.consume(FLOAT)
        elif self.current_token.type == CHAR:
            self.consume(CHAR)
        elif self.current_token.type == BOOL:
            self.consume(BOOL)

        node = VariableType(token)
        return node

    def variable_declaration(self):
        """
        A variable declaration rule should start with the variable name (ID) and optionally
        followed by COMMA and another ID. Default value can also be explicitly specified.
        It should end with AS and a variable_type as written in the rule below.

        variable_declaration : ID (COMMA ID [= default_value])* AS variable_type

        ------- ID[=default_value]--------> AS --------> variable_type
                ^                   |
                |                   |
                --------COMMA-------
        """

        # Create a node for the first Variable ID
        node = VariableId(self.current_token)
        var_id_nodes = [node]
        self.consume(ID)

        # Loop to create nodes for other declaration (if there is)
        while self.current_token.type == COMMA:
            self.consume(COMMA)
            node = VariableId(self.current_token)
            var_id_nodes.append(node)
            self.consume(ID)

        # Expect for next token type to be "AS"
        self.consume(AS)

        # Create a node for the variable type
        var_type_node = self.variable_type()

        # Create a variable declaration nodes using var_node and type_node
        variable_declaration = []
        for var_id_node in var_id_nodes:
            variable_declaration.append(VariableDeclaration(var_id_node, var_type_node))

        return variable_declaration

    def variable_declarations(self):
        """
        A variable_declarations rule should start with VAR and followed by one or more
        variable_declaration as written in the rule below.

        variable_declarations : VAR (variable_declaration)+

        VAR ----> variable_declaration ------
             ^                          |
             |                          |
             ----------------------------
        """
        declarations = []
        while self.current_token.type == VAR:
            self.consume(VAR)
            if self.current_token.type == ID:
                var_declaration = self.variable_declaration()
                declarations.extend(var_declaration)

        return declarations

    def program_start(self):
        """
        A code_block rule starts with variable declarations as written in the rule below.

        code_block : variable_declarations
        """
        variable_declarations_nodes = self.variable_declarations()
        node = ProgramStart(variable_declarations_nodes)
        return node

    def parse(self):
        return self.program_start()
