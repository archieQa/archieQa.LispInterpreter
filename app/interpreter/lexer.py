import re

# Token types
NUMBER = 'NUMBER'
SYMBOL = 'SYMBOL'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'


def tokenize(input_text):
    """Tokenizes the input Lisp code."""
    tokens = []

    # Remove comments by ignoring anything from ; to end of line
    input_text = re.sub(r';.*', '', input_text)  # Strip comments from input text

    # Update the SYMBOL pattern to include +, -, *, /
    token_specification = [
        (NUMBER, r'\d+(\.\d*)?'),  # Integer or decimal number
        (SYMBOL, r'[a-zA-Z_+\-*/][a-zA-Z0-9_+\-*/]*'),  # Symbols including operators
        (LPAREN, r'\('),  # Opening parenthesis
        (RPAREN, r'\)'),  # Closing parenthesis
    ]

    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

    for match in re.finditer(tok_regex, input_text):
        kind = match.lastgroup
        value = match.group()
        tokens.append((kind, value))

    # Debugging: print tokens to verify SYMBOL tokens
    print("Tokens:", tokens)

    return tokens
