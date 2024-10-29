from app.interpreter.lexer import tokenize
from app.interpreter.parser import parse
from app.interpreter.evaluator import evaluate
from app.interpreter.environment import Environment
from app.interpreter.exceptions import LispError
from app.interpreter.logger import log_error, log_evaluation  # Import logging functions


def repl():
    """A simple Read-Eval-Print Loop (REPL) for the Lisp interpreter."""
    env = Environment()
    print("Simple Lisp Interpreter. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("lisp> ")
            if user_input.strip().lower() == "exit":
                print("Exiting Lisp interpreter. Goodbye!")
                break

            tokens = tokenize(user_input)
            ast = parse(tokens)
            result = evaluate(ast, env)

            # Format output to remove unnecessary decimals
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print(result)

        except LispError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    repl()
