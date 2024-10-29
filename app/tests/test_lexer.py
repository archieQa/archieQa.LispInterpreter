import unittest
from interpreter.lexer import tokenize, NUMBER, SYMBOL, LPAREN, RPAREN


class TestLexer(unittest.TestCase):
    def test_tokenize_numbers_and_symbols(self):
        input_text = "(define x 10)"
        tokens = tokenize(input_text)
        expected_tokens = [
            (LPAREN, '('),
            (SYMBOL, 'define'),
            (SYMBOL, 'x'),
            (NUMBER, '10'),
            (RPAREN, ')')
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_nested_expression(self):
        input_text = "(+ 1 (* 2 3))"
        tokens = tokenize(input_text)
        expected_tokens = [
            (LPAREN, '('),
            (SYMBOL, '+'),
            (NUMBER, '1'),
            (LPAREN, '('),
            (SYMBOL, '*'),
            (NUMBER, '2'),
            (NUMBER, '3'),
            (RPAREN, ')'),
            (RPAREN, ')')
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_empty_input(self):
        tokens = tokenize("")
        self.assertEqual(tokens, [])  # Expect an empty
