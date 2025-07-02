from enum import StrEnum, auto
from dataclasses import dataclass
from utils import Green, Red, Cyan, Purple, Yellow

KEYWORDS = ("let", "num", "str", "null", "print", "if", "else", "while", "fn", "return", "continue", "break")

class TokenType(StrEnum):
    KEYWORD = auto()
    KW_LET = auto()
    KW_NUM = auto()
    KW_STR = auto()
    KW_NULL = auto()
    KW_PRINT = auto()
    KW_IF = auto()
    KW_ELSE = auto()
    KW_WHILE = auto()
    KW_FN = auto()
    KW_RETURN = auto()
    KW_CONTINUE = auto()
    KW_BREAK = auto()

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
    EOF = auto()

KEYWORDS = {
    "let": TokenType.KW_LET,
    "num": TokenType.KW_NUM,
    "str": TokenType.KW_STR,
    "null": TokenType.KW_NULL,
    "print": TokenType.KW_PRINT,
    "if": TokenType.KW_IF,
    "else": TokenType.KW_ELSE,
    "while": TokenType.KW_WHILE,
    "fn": TokenType.KW_FN,
    "return": TokenType.KW_RETURN,
    "continue": TokenType.KW_CONTINUE,
    "break": TokenType.KW_BREAK
}
@dataclass
class Token:
    token_type: TokenType
    value: str | None

    def __repr__(self):
        return f"{Green(self.token_type.value.upper())} {Cyan(self.value)}"

def get_tokens(code: str) -> list[Token]:
    tokens = []
    i = 0
    
    while i < len(code):
        if code[i] == ' ':
            i += 1
            continue

        if code[i] == '#':
            while code[i] != '\n':
                i+=1
            i+=1
            continue
        
        if code[i] == '\n':
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
        if code[i] == '>':
            if code[i+1] == '=':
                tokens.append(Token(TokenType.GREATER_OR_EQUAL, code[i:i+2])) #assuming this doesnt exceed the max length?
            else:
                tokens.append(Token(TokenType.GREATER_THAN, code[i]))
            i+=1
            continue
        if code[i] == '<':
            if code[i+1] == '=':
                tokens.append(Token(TokenType.LESS_OR_EQUAL, code[i:i+2])) #same as that ^
            else:
                tokens.append(Token(TokenType.LESS_THAN, code[i]))
            i+=1
            continue
        if code[i] == '=':
            if code[i+1] == '=':
                tokens.append(Token(TokenType.EQUAL, "=="))
            else:
                tokens.append(Token(TokenType.ASSIGN, "="))
            i+=1
            continue
        if code[i] == ':':
            tokens.append(Token(TokenType.COLON, ':'))
            i+=1
            continue
        if code[i] == ';':
            tokens.append(Token(TokenType.SEMICOLON, ';'))
            i+=1
            continue
        if code[i] == ',':
            tokens.append(Token(TokenType.COMMA, ','))
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
        
        if code[i].isalpha():
            start = i
            i += 1
            while(code[i].isalnum() or code[i] == '_'):
                i+= 1
            if code[start:i] in KEYWORDS:
                tokens.append(Token(KEYWORDS[code[start:i]], code[start:i]))
            else:
                tokens.append(Token(TokenType.IDENTIFIER, code[start:i]))
            continue
    return tokens


if __name__ == "__main__":
    with open("sample5.mb", "r") as f:
        code = f.read()
    tokens = get_tokens(code)
    for token in tokens:
        print(token)

