import unittest
from interpreter.lexer import tokenize
from interpreter.parser import parse
from interpreter.evaluator import evaluate
from interpreter.environment import Environment
from interpreter.exceptions import ArgumentError


class TestLambda(unittest.TestCase):
    def setUp(self):
        self.env = Environment()  # Create a new environment for each test

    def test_basic_lambda(self):
        tokens = tokenize("((lambda (x) (* x x)) 5)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)
        self.assertEqual(result, 25)

    def test_lambda_with_addition(self):
        tokens = tokenize("(define square (lambda (x) (* x x)))")
        ast = parse(tokens)
        evaluate(ast, self.env)  # Define the square function

        tokens = tokenize("(square 4)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)  # Call square with argument 4
        self.assertEqual(result, 16)

    def test_nested_lambda(self):
        tokens = tokenize("(define adder (lambda (x) (lambda (y) (+ x y))))")
        ast = parse(tokens)
        evaluate(ast, self.env)  # Define adder function that returns a lambda

        tokens = tokenize("((adder 5) 10)")
        ast = parse(tokens)
        result = evaluate(ast, self.env)  # Call adder with nested lambda
        self.assertEqual(result, 15)

    def test_lambda_missing_body(self):
        tokens = tokenize("(lambda (x))")
        ast = parse(tokens)
        with self.assertRaises(ArgumentError):  # Expect an ArgumentError due to missing body
            evaluate(ast, self.env)


if __name__ == '__main__':
    unittest.main()
