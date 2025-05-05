#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError
    except ValueError:
        print("Error: argument must be a non-negative integer", file=sys.stderr)
        sys.exit(1)
    print(factorial(num))
