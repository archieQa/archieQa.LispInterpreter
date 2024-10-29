from app.interpreter.builtins import builtins  # Import the dictionary of built-in functions
from app.interpreter.exceptions import UndefinedSymbolError  # Import custom exception for undefined symbols


class Environment:
    def __init__(self, parent=None, bindings=None):
        self.variables = {} if parent else builtins.copy()  # Start with built-ins if no parent environment
        self.parent = parent
        if bindings:
            self.variables.update(bindings)

    def define(self, var_name, value):
        """Adds a new variable to the environment."""
        self.variables[var_name] = value

    def lookup(self, name):
        """Retrieves a variable or function by name."""
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            raise NameError(f"Undefined symbol: {name}")
