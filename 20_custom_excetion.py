# Step 1: Define custom exception
class InvalidAgeError(Exception):
    pass  # We don't need to add anything extra here unless we want a custom message

# Step 2: Define function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")  # Raise the custom exception
    else:
        print("Access granted.")

# Step 3: Use try-except to handle exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Access denied:", e)
except ValueError:
    print("Please enter a valid number.")
