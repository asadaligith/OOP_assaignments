class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the factor when object is created

    def __call__(self, number):
        return number * self.factor  # Called when object is used like a function

# Create an object with a factor of 5
multiply_by_5 = Multiplier(5)

# Test if the object is callable
print("Is object callable?", callable(multiply_by_5))  # Should print: True

# Use the object like a function
result = multiply_by_5(10)  # Should return 10 * 5 = 50
print("Result of multiply_by_5(10):", result)
