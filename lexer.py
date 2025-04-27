from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()

    KEYWORD = auto()
    KW_PRINT = auto()

    ARITHMETIC_OP = auto()
    LOGICAL_OP = auto()
    COMPARISON_OP = auto()

    SEPARATOR = auto()

    EOF = auto()
@dataclass
class Token:
    tokentype: TokenType
    value: str

class Buffer:
    def __init__(self):
        self.buffer = ''
    def add(self, c):
        self.buffer += c
    def flush(self):
        self.buffer = ''
    def __repr__(self):
        return self.buffer
KEYWORDS = ["print", "num", "str", "if", "else", "while", "continue", "break", "fn", "return", "null", "true", "false"]
SEPARATORS = ["#", ",", ";", "(", ")", ""]
OPERATORS = []



filepath = "./sample.mb"
with open(filepath, 'r') as f: code = f.read()


tokens = []
i = 0
codelen = len(code)
buffer = Buffer()
while i < codelen:
    if code[i] == '#':
        tokens.append(Token(TokenType.SEPARATOR, code[i]))
    if code[i] == "\n":
        tokens.append(Token(TokenType.SEPARATOR, code[i]))
        
    i+=1

print(tokens)
    
