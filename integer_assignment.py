# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
product = 1
for i in range(1, 11):
    product *= i
print(f"Product: {product}")

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
remainder = 156 % 7
print(f"Remainder: {remainder}")

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
square = 25 ** 2
print(f"Square: {square}")

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
cube_root = 125 ** (1/3)
print(f"Cube Root: {cube_root}")

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
num = 12345
digit_sum = sum(int(digit) for digit in str(num))
print(f"Sum of digits: {digit_sum}")

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
n = 97
is_prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"97 is prime? {is_prime}")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
factorial = 1
for i in range(1, 9):
    factorial *= i
print(f"Factorial: {factorial}")

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
nums = [15, 23, 31, 42, 56]
average = sum(nums) / len(nums)
print(f"Average: {average}")

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
import math
gcd = math.gcd(48, 36)
print(f"GCD: {gcd}")

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
odds = [2*i+1 for i in range(20)]
sum_odds = sum(odds)
print(f"First 20 odd numbers: {odds}")
print(f"Sum: {sum_odds}")
