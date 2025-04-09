# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample number
num = 9

# Calling the function and printing the output
print(f"The factorial of {num} is {factorial(num)}")