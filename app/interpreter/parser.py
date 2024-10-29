from app.interpreter.lexer import LPAREN, RPAREN, NUMBER, SYMBOL

def parse(tokens):
    """Parses tokens into an Abstract Syntax Tree (AST)."""

    def parse_expression(index):
        token_type, token_value = tokens[index]

        if token_type == NUMBER:
            print(f"Parsing NUMBER: {token_value}")  # Debugging
            return float(token_value), index + 1  # Convert numeric strings to float or int
        elif token_type == SYMBOL:
            return token_value, index + 1
        elif token_type == LPAREN:
            index += 1
            expr = []
            while tokens[index][0] != RPAREN:
                sub_expr, index = parse_expression(index)
                expr.append(sub_expr)
            return expr, index + 1
        else:
            raise SyntaxError(f"Unexpected token: {token_value}")

    ast, _ = parse_expression(0)
    return ast
