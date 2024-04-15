# 2) WAP to perform Lexical analysis on int a,b,c;

import re

def lexical_analyzer(program):
    tokens = re.findall(r'\b\w+\b|\S', program)
    print('\n'.join(f"{token} = {'Keyword' if token in keywords else 'Operator' if token in operators else 'Separator' if token in separators else 'Identifier'}" for token in tokens))

keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum",
            "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

operators = ['+', '-', '*', '/', '>', '<', '=']

separators = [';', ',', '(', ')', '[', ']', '{', '}']

if __name__ == "__main__":
    user_input = input("Enter the program:\n")
    lexical_analyzer(user_input)