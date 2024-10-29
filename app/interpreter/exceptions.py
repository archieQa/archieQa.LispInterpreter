class LispError(Exception):  # Base class for all Lisp-related errors
    """General error for the Lisp interpreter."""
    pass

class UndefinedSymbolError(LispError):  # Error for undefined symbols
    """Raised when a symbol is not found in the environment."""
    pass

class ArgumentError(LispError):  # Error for incorrect argument counts
    """Raised when an operation receives an incorrect number of arguments."""
    pass

class SyntaxError(LispError):  # Error for invalid syntax
    """Raised when there is a syntax error in the input."""
    pass
