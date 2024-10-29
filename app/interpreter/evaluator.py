from app.interpreter.environment import Environment
from app.interpreter.exceptions import ArgumentError, SyntaxError


def evaluate(ast, env):
    """Evaluates the Abstract Syntax Tree (AST) in the given environment."""

    if isinstance(ast, float):
        return ast  # Return the number directly as a result

    elif isinstance(ast, str):
        return env.lookup(ast)  # Retrieve the symbol's value from the environment

    elif isinstance(ast, list):
        if len(ast) == 0:
            raise SyntaxError("Empty expression")

        op = ast[0]

        if op == 'define':
            if len(ast) != 3:
                raise ArgumentError(f"'define' expects 2 arguments, got {len(ast) - 1}")
            _, var_name, expr = ast
            env.define(var_name, evaluate(expr, env))
            return None

        elif op == 'lambda':
            if len(ast) != 3:
                raise ArgumentError(f"'lambda' expects 2 arguments, got {len(ast) - 1}")
            _, params, body = ast
            return lambda *args: evaluate(body, Environment(parent=env, bindings=dict(zip(params, args))))

        elif op == 'if':
            if len(ast) != 4:
                raise ArgumentError(f"'if' expects 3 arguments, got {len(ast) - 1}")
            _, condition, true_branch, false_branch = ast
            condition_result = evaluate(condition, env)  # Evaluate the condition expression
            return evaluate(true_branch if condition_result else false_branch, env)

        else:
            # Check if op is callable and handle nested expressions
            func = env.lookup(op)  # Lookup the operator in the environment

            # If op is not a function, raise an error
            if not callable(func):
                raise ArgumentError(f"'{op}' is not callable")

            # Evaluate arguments and apply function
            args = [evaluate(arg, env) for arg in ast[1:]]  # Evaluate each argument
            return func(*args)

    else:
        raise SyntaxError(f"Unexpected AST node: {ast}")
