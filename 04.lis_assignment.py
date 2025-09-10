# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1
print("Question 1:")
squares = [i**2 for i in range(1, 11)]
print(squares)

# Question 2
print("\nQuestion 2:")
nums = [1,2,3,4,5,6,7,8,9,10]
print(sum([x for x in nums if x%2==0]))

# Question 3
print("\nQuestion 3:")
dup_list = [1,2,2,3,4,4,5,6,6,7]
print(list(set(dup_list)))

# Question 4
print("\nQuestion 4:")
lst = [64, 34, 25, 12, 22, 11, 90]
print(sorted(lst, reverse=True))

# Question 5
print("\nQuestion 5:")
nums = [15, 23, 31, 42, 56, 78, 91]
print(sum(nums)/len(nums))

# Questio
