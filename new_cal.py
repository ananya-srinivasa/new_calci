"""
This module provides functions for addition and subtraction operations.
"""

def add(number1, number2):
    """
    Adds two numbers and returns the result.
    """
    total = number1 + number2
    return total

def subtract(number1, number2):
    """
    Subtracts the second number from the first number and returns the result.
    """
    total = number1 - number2
    return total

ADDING = add(12, 3)
SUBTRACTING = subtract(10, 6)
TOTAL = ADDING - SUBTRACTING
print("Total:", TOTAL)
