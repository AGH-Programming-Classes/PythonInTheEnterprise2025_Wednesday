def greet_user(name: str) -> str:
    if not name:
        name = "User"
    return f"Hello, {name}! Welcome to the Hello World project."
