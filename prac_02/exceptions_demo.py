"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur when the input numerator and denominator are invalid numbers.
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur when input denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   The input must be greater than 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator which is greater than 0: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")