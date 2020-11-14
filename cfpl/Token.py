"""
File:           Token.py
Description:    A Token class contains the token type and its value
Author:         Louis Albert Apas (louisalbertapas25@gmail.com)

Copyright 2020
"""


class Token(object):
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
