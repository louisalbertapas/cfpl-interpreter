"""
File:           Interpreter.py
Description:    An Interpreter class that reads through the Abstract Syntax Tree using visitor pattern
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""
from cfpl.AbstractSyntaxTree import BinOp, UnaryOp, Char, Bool, VariableId
from constants.reserved_keywords import *
from constants.debug import *


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + node.name
        visitor = getattr(self, method_name, self.generic_visit)
        if debug:
            print(method_name)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(node.name))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.output = ''
        self.input = []

        # Store variables in these dictionaries
        # 'ID' : type
        # 'ID' : value
        self.SYMBOL_TABLE_TYPE = {}
        self.SYMBOL_TABLE_VALUE = {}

    def add_variable_value_to_symbol_table(self, name, value):
        # Check if name / ID exists in the SYMBOL_TABLE_TYPE
        if name in self.SYMBOL_TABLE_TYPE:
            if self.SYMBOL_TABLE_TYPE[name] == INT:
                try:
                    value = int(value)
                except ValueError:
                    raise ValueError('Value ' + repr(value) + ' is not an INT type')
                if isinstance(value, int):
                    self.SYMBOL_TABLE_VALUE[name] = value
                else:
                    raise ValueError('Value ' + repr(value) + ' is not an INT type')
            elif self.SYMBOL_TABLE_TYPE[name] == FLOAT:
                try:
                    value = float(value)
                except ValueError:
                    raise ValueError('Value ' + repr(value) + ' is not a FLOAT type')
                if isinstance(value, float):
                    self.SYMBOL_TABLE_VALUE[name] = value
                else:
                    raise NameError('Value ' + repr(value) + ' is not a FLOAT type')
            elif self.SYMBOL_TABLE_TYPE[name] == CHAR:
                if isinstance(value, str):
                    self.SYMBOL_TABLE_VALUE[name] = value
                else:
                    raise NameError('Value ' + repr(value) + ' is not a CHAR type')
            elif self.SYMBOL_TABLE_TYPE[name] == BOOL:
                if isinstance(value, bool):
                    self.SYMBOL_TABLE_VALUE[name] = value
                elif value in ['TRUE', 'FALSE']:
                    if value == 'TRUE':
                        value = True
                    else:
                        value = False
                    self.SYMBOL_TABLE_VALUE[name] = value
                else:
                    raise ValueError('Value ' + repr(value) + ' is not a BOOL type')
            else:
                raise NameError('Unknown data type ' + self.SYMBOL_TABLE_TYPE[name])

    def visit_bin_op(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == MOD:
            return self.visit(node.left) % self.visit(node.right)
        elif node.op.type == ASSIGN:
            value = self.visit(node.right)
            if node.value is None:
                node.value = value
            if node.left.name == 'bin_op':
                node.left.value = node.value
                return self.visit(node.left)
            if node.left.name == 'variable_id' and node.left.value in self.SYMBOL_TABLE_VALUE:
                self.add_variable_value_to_symbol_table(node.left.value, node.value)
            if type(node.right).__name__ == 'variable_id' and node.right.value in self.SYMBOL_TABLE_VALUE:
                self.add_variable_value_to_symbol_table(node.right.value, node.value)
            return value
        elif node.op.type == GREATER_THAN:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == GREATER_EQUAL:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == LESSER_THAN:
            return self.visit(node.left) < self.visit(node.right)
        elif node.op.type == LESSER_EQUAL:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == EQUAL:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == NOT_EQUAL:
            return not (self.visit(node.left) == self.visit(node.right))
        elif node.op.type == AND:
            return self.visit(node.left) and self.visit(node.right)
        elif node.op.type == OR:
            return self.visit(node.left) or self.visit(node.right)

    def visit_unary_op(self, node):
        op = node.op.type
        if op == PLUS:
            return self.visit(node.expr) * 1
        elif op == MINUS:
            return self.visit(node.expr) * -1
        elif node.op.type == NOT:
            return not self.visit(node.expr)

    def visit_no_op(self, node):
        pass

    def visit_num(self, node):
        return node.value

    def visit_char(self, node):
        return node.value

    def visit_bool(self, node):
        return node.value

    def visit_string(self, node):
        return node.value

    def visit_variable_id(self, node):
        try:
            variable_id = node.value
            variable_value = self.SYMBOL_TABLE_VALUE[variable_id]
            return variable_value
        except KeyError:
            raise NameError('Name ' + repr(variable_id) + ' is not defined at line ' + str(node.line + 1))

    def visit_program_start(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statements)

    def visit_compound_statements(self, node):
        for child in node.children:
            if child is not None:
                self.visit(child)

    def visit_assign(self, node):
        values = [node.left]
        if type(node.left.value).__name__ == 'list':
            values = []
            for val in node.left.value:
                values.append(val)
        for val in values:
            var_name = val.value
            if val.token.type != STRING_CONST and var_name not in self.SYMBOL_TABLE_VALUE:
                raise NameError('Name ' + repr(var_name) + ' is not defined at line ' + str(val.line + 1))
            self.add_variable_value_to_symbol_table(var_name, self.visit(node.right))

    def visit_output(self, node):
        for val in node.value:
            if val.name == 'variable_id':
                if val.value not in self.SYMBOL_TABLE_VALUE:
                    raise NameError('Name ' + repr(val.value) + ' is not defined at line ' + str(val.line + 1))
                val_name = val.value
                val = self.SYMBOL_TABLE_VALUE[val_name]
                data_type = self.SYMBOL_TABLE_TYPE[val_name]
                if data_type == INT:
                    val = int(val)
                elif data_type == FLOAT:
                    val = float(val)
                elif data_type == CHAR:
                    val = val[0] if len(val) > 0 else val
                elif data_type == BOOL:
                    if type(val) is bool:
                        val = 'TRUE' if val else 'FALSE'
                    val = str(val)
                    if val not in ['TRUE', 'FALSE']:
                        val = 'FALSE'
                else:
                    val = str(val)
            else:
                val = val.value
            self.output += str(val)
        return node.value

    def visit_input(self, node):
        i = 0
        if len(node.value) != len(self.input):
            raise NameError("Incorrect number of input parameters. Error in line " + str(node.line))
        for val in node.value:
            self.add_variable_value_to_symbol_table(val.value, self.input[i])
            i += 1

        self.input = []
        return node.value

    def visit_if_else(self, node):
        bool_expr = self.visit(node.expr)
        if bool_expr and bool_expr != "FALSE":  # add additional checking if not FALSE
            values = [node.value]
            if type(node.value).__name__ == 'list':
                values = []
                for val in node.value:
                    values.append(val)
            for val in values:
                self.visit(val)
        else:
            if node.else_token is not None:
                self.visit(node.else_token)
        return node.value

    def visit_while(self, node):
        while True:
            bool_expr = self.visit(node.expr)
            if not bool_expr or bool_expr == "FALSE":
                # end while loop
                break
            values = [node.value]
            if type(node.value).__name__ == 'list':
                values = []
                for val in node.value:
                    values.append(val)
            for val in values:
                self.visit(val)

        return node.value

    def visit_variable_declaration(self, node):
        if node.var_id_node.value in self.SYMBOL_TABLE_TYPE:
            raise NameError("Redeclaration of variable " + repr(node.var_id_node.value))
        if node.var_id_node.default_value is None:
            if node.var_type_node.value == INT:
                default_value = 0
            elif node.var_type_node.value == FLOAT:
                default_value = 0.0
            elif node.var_type_node.value == CHAR:
                default_value = ''
            elif node.var_type_node.value == BOOL:
                default_value = 'FALSE'
        else:
            node_default_value = node.var_id_node.default_value
            if type(node_default_value) == BinOp:
                default_value = self.visit_bin_op(node_default_value)
            elif type(node_default_value) == UnaryOp:
                default_value = self.visit_unary_op(node_default_value)
            elif type(node_default_value) == Char:
                default_value = self.visit_char(node_default_value)
            elif type(node_default_value) == Bool:
                default_value = self.visit_bool(node_default_value)
            elif type(node_default_value) == VariableId:
                default_value = self.visit_variable_id(node_default_value)
            else:
                # VariableId
                default_value = node_default_value.value

        # Add to the SYMBOL_TABLE_TYPE the var_id and its corresponding var_type
        self.SYMBOL_TABLE_TYPE[node.var_id_node.value] = node.var_type_node.value

        # Add to the SYMBOL_TABLE_VAR the value for the respective var_id
        self.add_variable_value_to_symbol_table(node.var_id_node.value, default_value)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
