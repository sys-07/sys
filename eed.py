
def extended_gcd(a, b):
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd
    """

    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def run_extended_euclidean():
    print("\nExtended Euclidean Algorithm")

    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))

    gcd, x, y = extended_gcd(a, b)

    print(f"GCD({a}, {b}) = {gcd}")
    print(f"Coefficients: x = {x}, y = {y}")
    print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")


run_extended_euclidean()
