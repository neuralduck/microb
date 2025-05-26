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
    OPEN_SQUARE = auto()
    CLOSE_SQUARE = auto()

    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()

    NEW_LINE = auto()

@dataclass
class Token:
    token_type: TokenType
    value: str | None

    def __repr__(self):
        return f"{self.token_type.value.upper()}: {self.value}"

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
    
    if code[i] == '+':
        tokens.append(Token(TokenType.ADD, code[i]))
        i+=1
        continue
    if code[i] == '-':
        tokens.append(Token(TokenType.SUB, code[i]))
        i+=1
        continue
    if code[i] == '*':
        tokens.append(Token(TokenType.MUL, code[i]))
        i+=1
        continue
    if code[i] == '/':
        tokens.append(Token(TokenType.DIV, code[i]))
        i+=1
        continue
    if code[i] == '%':
        tokens.append(Token(TokenType.MOD, code[i]))
        i+=1
        continue
    if code[i] == '(':
        tokens.append(Token(TokenType.OPEN_PAREN, code[i]))
        i+=1
        continue
    if code[i] == ')':
        tokens.append(Token(TokenType.CLOSE_PAREN, code[i]))
        i+=1
        continue
    if code[i] == '{':
        tokens.append(Token(TokenType.OPEN_BRACE, code[i]))
        i+=1
        continue
    if code[i] == '}':
        tokens.append(Token(TokenType.CLOSE_BRACE, code[i]))
        i+=1
        continue
    if code[i] == '[':
        tokens.append(Token(TokenType.OPEN_SQUARE, code[i]))
        i+=1
        continue
    if code[i] == ']':
        tokens.append(Token(TokenType.CLOSE_SQUARE, code[i]))
        i+=1
        continue
    
    if code[i] == '"':
        i += 1
        start = i #next character after first "
        while (code[i] != '"'): #breaks at second " with i pointing to the second "
            i += 1
        # print("string literal")
        # print(code[start:i]) #prints without "" included
        tokens.append(Token(TokenType.STRING_LITERAL, code[start:i]))
        i += 1 #shift i to the character after second "


        continue
    
    if code[i].isnumeric():
        start = i #starting index of the number
        i += 1
        while(code[i].isnumeric() or code[i] == '.'): #when this breaks i will point to the char after the number
            i+=1
        #print("number literal")
        #print(code[j:i])
        tokens.append(Token(TokenType.NUMBER_LITERAL, code[start:i]))
        continue
    
    i+=1

for token in tokens:
    print(token, '\n')
        
