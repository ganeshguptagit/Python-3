# Python-3

**Task 1: Calculate Factorial Using a Function**

```

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

```

**Output:**

![Screenshot 2025-04-09 142542](https://github.com/user-attachments/assets/eb2dadbb-6238-45fb-a689-c4ac09f44416)

**Task 2: Using the Math Module for Calculations**

```

#Importing Maths from Modules.

import math

# Asking the user for a number
num = float(input("Enter a number: "))

# Calculating and displaying results
print(f"Square root of {num}: {math.sqrt(num)}")
print(f"Natural logarithm (log base e) of {num}: {math.log(num)}")
print(f"Sine of {num} (in radians): {math.sin(num)}")

```

**Output:**

![Screenshot 2025-04-09 142913](https://github.com/user-attachments/assets/90288224-1df2-4e69-966e-7368b05c29c8)

