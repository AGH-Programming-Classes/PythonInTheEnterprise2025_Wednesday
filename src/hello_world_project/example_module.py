def log_calculation(expression, result):
    """Example function to log calculations to a file."""
    with open("calculation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{expression} = {result}\n")
