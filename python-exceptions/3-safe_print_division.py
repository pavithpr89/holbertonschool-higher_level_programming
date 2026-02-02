#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide 2 integers and print the result safely."""
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
