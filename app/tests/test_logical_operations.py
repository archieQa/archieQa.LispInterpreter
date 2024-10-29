import unittest
from interpreter.lexer import tokenize
from interpreter.parser import parse
from interpreter.evaluator import evaluate
from interpreter.environment import Environment

class TestLogicalOperations(unittest.TestCase):
    def setUp(self):
        self.env = Environment()  # Create a new environment for each test

    def test_logical_and(self):
        tokens = tokenize("(and True True False)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertFalse(result)

        tokens = tokenize("(and True True True)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertTrue(result)

    def test_logical_or(self):
        tokens = tokenize("(or False False True)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertTrue(result)

        tokens = tokenize("(or False False False)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertFalse(result)

    def test_logical_not(self):
        tokens = tokenize("(not True)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertFalse(result)

        tokens = tokenize("(not False)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertTrue(result)

    def test_non_boolean_and(self):
        tokens = tokenize("(and 1 2 0)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertFalse(result)  # Expect False because of 0

if __name__ == '__main__':
    unittest.main()
