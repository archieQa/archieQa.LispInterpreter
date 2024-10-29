# Arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero")
    return x / y

# Logical and comparison functions
def greater_than(x, y):  # >
    return x > y

def less_than(x, y):  # <
    return x < y

def greater_equal(x, y):  # >=
    return x >= y

def less_equal(x, y):  # <=
    return x <= y

def logical_and(*args):
    return all(args)

def logical_or(*args):
    return any(args)

def logical_not(x):
    return not x

def list_func(*args):
    return list(args)

def car(lst):
    if not lst:
        raise ValueError("car called on empty list")
    return lst[0]

def cdr(lst):
    if not lst:
        raise ValueError("cdr called on empty list")
    return lst[1:]

def cons(x, lst):
    return [x] + lst

# Dictionary of built-in functions and constants
builtins = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'list': list_func,
    'car': car,
    'cdr': cdr,
    'cons': cons,
    'and': logical_and,
    'or': logical_or,
    'not': logical_not,
    '>': greater_than,      # Comparison operator
    '<': less_than,         # Comparison operator
    '>=': greater_equal,    # Comparison operator
    '<=': less_equal,       # Comparison operator
    'True': True,           # Boolean constant
    'False': False          # Boolean constant
}