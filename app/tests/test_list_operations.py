import unittest
from interpreter.lexer import tokenize
from interpreter.parser import parse
from interpreter.evaluator import evaluate
from interpreter.environment import Environment
from interpreter.exceptions import ArgumentError

class TestListOperations(unittest.TestCase):
    def setUp(self):
        self.env = Environment()  # Create a new environment for each test

    def test_list_creation(self):
        tokens = tokenize("(list 1 2 3)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertEqual(result, [1, 2, 3])

    def test_car_function(self):
        tokens = tokenize("(car (list 1 2 3))")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertEqual(result, 1)

    def test_cdr_function(self):
        tokens = tokenize("(cdr (list 1 2 3))")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertEqual(result, [2, 3])

    def test_cons_function(self):
        tokens = tokenize("(cons 0 (list 1 2 3))")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertEqual(result, [0, 1, 2, 3])

    def test_car_empty_list(self):
        tokens = tokenize("(car (list))")
        ast = parse(tokens)
        with self.assertRaises(ValueError):  # Expect ValueError for car on empty list
            evaluate(ast, self.env)

    def test_cdr_empty_list(self):
        tokens = tokenize("(cdr (list))")
        ast = parse(tokens)
        with self.assertRaises(ValueError):  # Expect ValueError for cdr on empty list
            evaluate(ast, self.env)

if __name__ == '__main__':
    unittest.main()
