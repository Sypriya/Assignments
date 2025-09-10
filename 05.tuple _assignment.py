# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1
print("Question 1: Create a tuple of first 10 natural numbers")
tuple_natural = tuple(range(1, 11))
print(tuple_natural)

# Question 2
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(t))

# Question 3
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
letters = ('a', 'b', 'c', 'd', 'e')
print(letters[2])

# Question 4
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
nums = (23, 45, 12, 67, 34, 89, 56)
print(max(nums))

# Question 5
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
t = (1, 5, 2, 5, 3, 5, 4, 5, 6)
print(t.count(5))

# Question 6
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
mixed_tuple = (10, 3.14, "hello", True)
print(mixed_tuple)

# Question 7
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
langs = ('java', 'python', 'c++', 'javascript')
print(langs.index('python'))

# Question 8
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
nums = (10, 20, 30, 40, 50)
print(25 in nums)

# Question 9
print("\nQuestion 9: Create a tuple of first 5 even numbers")
evens = tuple([2*i for i in range(1, 6)])
print(evens)

# Question 10
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
nums = (15, 23, 31, 42, 56, 78)
avg = sum(nums) / len(nums)
print(avg)
