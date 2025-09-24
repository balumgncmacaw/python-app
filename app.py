def add(a: inst, b: int) -> int: 
    """Return the sum of two number."""
    return a + b

def sub(a: inst, b: int) -> int: 
    """Return the difference of two number."""
    return a - b

if __name__ == "__main__":
    print("Hello from Python app")
    print("2 + 3 =" add(2, 3))
    print("5 -2 =",sub(5, 2))

