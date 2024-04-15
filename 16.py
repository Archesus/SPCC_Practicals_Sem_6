import re

def lex(expression):
    token_exprs = [
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
        (r'=', 'ASSIGN'),
        (r'\+', 'PLUS'),
        (r'\*', 'MULT'),
        (r'\(', 'LPAREN'),
        (r'\)', 'RPAREN'),
        (r'\d+', 'NUMBER'),
        (r'\s+', 'WHITESPACE')
    ]
    tokens = []
    for pattern, tag in token_exprs:
        for value in re.findall(pattern, expression):
            tokens.append((value, tag))
    return tokens

# Test the lexer
expression = "c = a * b + d"
tokens = lex(expression)

# Print each token along with its description
for token, tag in tokens:
    if tag == 'IDENTIFIER':
        print(f"{token}: Identifier")
    elif tag == 'ASSIGN':
        print(f"{token}: Assignment operator")
    elif tag == 'PLUS':
        print(f"{token}: Addition operator")
    elif tag == 'MULT':
        print(f"{token}: Multiplication operator")
    elif tag == 'LPAREN':
        print(f"{token}: Left Parenthesis")
    elif tag == 'RPAREN':
        print(f"{token}: Right Parenthesis")
    elif tag == 'NUMBER':
        print(f"{token}: Number")
