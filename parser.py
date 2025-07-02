from dataclasses import dataclass
from enum import StrEnum, auto
from lexer import get_tokens, Token, TokenType

class DataType(StrEnum):
    NUM = auto()
    STR = auto()
@dataclass
class Node:
    pass

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass


@dataclass
class PrintNode(Statement):
    value: Expression

@dataclass
class DeclarationNode(Statement):
    data_type: DataType
    var_name: str
    value: Expression
@dataclass
class AssignmentNode(Statement):
    var_name: str    
    value: Expression

def parse_statement(tokens: list[Token], pos: int):
    if tokens[pos].token_type == TokenType.IDENTIFIER:
        if tokens[pos+1] == TokenType.COLON:
            if tokens[pos+2] in (TokenType.KW_NUM, TokenType.KW_STR):
                if tokens[pos+3] == TokenType.ASSIGN:
                    if tokens[pos+4] in (TokenType.NUMBER_LITERAL, TokenType.STRING_LTIERAL):
                        return DeclarationNode() 



def build_ast(tokens: list[Token]):
    pass