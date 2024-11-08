class Calculator:
    def __init__(self, precision=10, max_input_value=1e100):
        # Initialize with default precision and maximum allowed input value.
        self.precision = precision
        self.max_input_value = max_input_value

    def add(self, a, b):
        # Add two numbers and round the result to the specified precision.
        return round(a + b, self.precision)

    def subtract(self, a, b):
        # Subtract the second number from the first and round the result.
        return round(a - b, self.precision)

    def multiply(self, a, b):
        # Multiply two numbers and round the result.
        return round(a * b, self.precision)

    def divide(self, a, b):
        # If dividing by zero, raise an error; otherwise, return the result.
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return round(a / b, self.precision)

    def power(self, a, b):
        # Raise a to the power of b and round the result.
        return round(a ** b, self.precision)

    def root(self, a, b):
        # Find the b-th root of a; raise an error if invalid.
        if a < 0 and b % 2 == 0:
            raise ValueError("Can't take the even root of a negative number!")
        return round(a ** (1 / b), self.precision)
