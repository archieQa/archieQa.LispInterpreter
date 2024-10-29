import unittest
from app.interpreter.lexer import tokenize
from app.interpreter.parser import parse

class TestParser(unittest.TestCase):
    def test_parse_simple_expression(self):
        tokens = tokenize("(+ 1 2)")
        ast = parse(tokens)
        expected_ast = ['+', 1.0, 2.0]  # Corrected expected value
        self.assertEqual(ast, expected_ast)

    def test_parse_nested_expression(self):
        tokens = tokenize("(+ 1 (* 2 3))")
        ast = parse(tokens)
        expected_ast = ['+', 1.0, ['*', 2.0, 3.0]]  # Corrected expected value
        self.assertEqual(ast, expected_ast)

    def test_parse_define_expression(self):
        tokens = tokenize("(define x 10)")
        ast = parse(tokens)
        expected_ast = ['define', 'x', 10.0]
        self.assertEqual(ast, expected_ast)

if __name__ == '__main__':
    unittest.main()
