from enum import StrEnum, auto
from dataclasses import dataclass


class TokenType(StrEnum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER_LITERAL = auto()
    STRING_LITERAL = auto()

    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()
    
    AND = auto()
    OR = auto()

    NOT = auto()
    
    EQUAL = auto()
    ASSIGN = auto()
    NOT_EQUAL = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_OR_EQUAL = auto()
    GREATER_OR_EQUAL = auto()

    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    OPEN_BRACE = auto()
    CLOSE_BRACE = auto()
    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()

    NEW_LINE = auto()

@dataclass
class Token:
    token_type: TokenType
    value: str | None

with open("sample.mb", "r") as f:
    code = f.read()

tokens = []
i = 0
buffer = ''

while i < len(code):
    if code[i] == ' ':
        i += 1
        continue

    if code[i] == '#':
        while code[i] != '\n':
            i+=1
        continue
    
    if code[i] == '"':
        i += 1
        j = i
        while code[i] != '"':
            i += 1
        #print("string literal")
        #print(code[j:i])
        tokens.append(Token(TokenType.STRING_LITERAL, code[j:i]))
    
    if code[i].isnumeric():
        j = i
        i += 1
        while(code[i].isnumeric() or code[i] == '.'):
            i+=1
        #print("number literal")
        #print(code[j:i])
        tokens.append(Token(TokenType.NUMBER_LITERAL, code[j:i]))
    
    i+=1

print(*tokens)
        
