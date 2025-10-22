import math

def safe_eval(expression):
    """Safely evaluate a mathematical expression."""
    # Można dodać bardziej zaawansowany parser zamiast eval
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    return eval(expression, {"__builtins__": {}}, allowed_names)

def is_operator(char):
    """Check if a character is a mathematical operator."""
    return char in "+-*/.**"
