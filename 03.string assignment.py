# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1
print("Question 1: Reverse the string 'Python Programming'")
print("Python Programming"[::-1])

# Question 2
print("\nQuestion 2: Check if 'racecar' is a palindrome")
s = "racecar"
print(s == s[::-1])

# Question 3
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
print(len("Python is a great programming language".split()))

# Question 4
print("\nQuestion 4: Convert 'hello world' to title case")
print("hello world".title())

# Question 5
print("\nQuestion 5: Find the length of string 'Data Science'")
print(len("Data Science"))

# Question 6
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
print("Machine Learning".replace(" ", "_"))

# Question 7
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
print("python" in "Python Programming Language".lower())

# Question 8
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
print("Artificial Intelligence"[:5])

# Question 9
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
print("UPPERCASE".lower())

# Question 10
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
vowels = "aeiouAEIOU"
print("".join(ch for ch in "Computer Science" if ch not in vowels))

# Question 11
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
s = "mississippi"
print(max(set(s), key=s.count))

# Question 12
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
print(sorted("listen") == sorted("silent"))

# Question 13
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
print("python programming language".title())

# Question 14
print("\nQuestion 14: Count consonants in 'Hello World'")
print(sum(1 for c in "Hello World" if c.isalpha() and c.lower() not in "aeiou"))

# Question 15
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
words = "Python is a programming language".split()
print(max(words, key=len))

# Question 16
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
import string
s = "Hello, World! How are you?"
print("".join(ch for ch in s if ch not in string.punctuation))

# Question 17
print("\nQuestion 17: Check if string starts with 'Python'")
print("Python Programming".startswith("Python"))

# Question 18
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
print("Hello World".find("o"))

# Question 19
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
print("apple,banana,orange".split(","))

# Question 20
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
print(" ".join(['Python', 'is', 'awesome']))

# Question 21
print("\nQuestion 21: Check if string contains only digits: '12345'")
print("12345".isdigit())

# Question 22
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
print("HelloWorld".isalpha())

# Question 23
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
s = "hello world"
print("".join(ch.upper() if i % 2 else ch.lower() for i, ch in enumerate(s)))

# Question 24
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
print([i for i, ch in enumerate("banana") if ch == "a"])

# Question 25
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
print("  Hello World  ".strip())

# Question 26
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
print("programming".endswith("ing"))

# Question 27
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
print("Hello World".replace("o", "0", 1))

# Question 28
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
words = "Python is a programming language".split()
print(min(words, key=len))

# Question 29
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
print(sum(1 for w in "Python programming is powerful".split() if w.lower().startswith("p")))

# Question 30
print("\nQuestion 30: Reverse words in 'Hello World Python'")
print(" ".join("Hello World Python".split()[::-1]))

# Question 31
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
import re
print(bool(re.match(r"[^@]+@[^@]+\.[^@]+", "user@example.com")))

# Question 32
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
print("https://www.example.com/path".split("/")[2])

# Question 33
print("\nQuestion 33: Count lines in multi-line string")
ml = """line1
line2
line3"""
print(len(ml.splitlines()))

# Question 34
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
print(set("hello") & set("world"))

# Question 35
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
print(bool(re.match(r"^\+?\d[\d\-]+$", "+1-555-123-4567")))

# Question 36
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
print(re.findall(r"\d+", "abc123def456ghi789"))

# Question 37
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
s = "snake_case"
parts = s.split("_")
print(parts[0] + "".join(p.capitalize() for p in parts[1:]))

# Question 38
print("\nQuestion 38: Check if string is a valid palindrome ignoring case")
s = "A man a plan a canal Panama"
cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
print(cleaned == cleaned[::-1])

# Question 39
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
words = "the quick brown fox jumps over the lazy dog".split()
print(max(set(words), key=words.count))

# Question 40
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
s = "National Aeronautics and Space Administration"
print("".join(word[0].upper() for word in s.split()))

# Question 41
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
s = "((()))"
stack = []
balanced = True
for ch in s:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if not stack:
            balanced = False
            break
        stack.pop()
print(balanced and not stack)

# Question 42
print("\nQuestion 42: Convert 'hello world' to Morse code")
morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", " ": "/"
}
print(" ".join(morse[ch] for ch in "hello world"))

# Question 43
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
def lcs(a, b):
    longest = ""
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            sub = a[i:j]
            if sub in b and len(sub) > len(longest):
                longest = sub
    return longest
print(lcs("programming", "grammar"))

# Question 44
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
print(bool(re.match(r"^https?://[^\s]+$", "https://www.google.com")))

# Question 45
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
print([w for w in "Python programming is amazing and powerful".split() if len(w) > 5])

# Question 46
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
def piglatin(word):
    return word[1:] + word[0] + "ay"
print(" ".join(piglatin(w) for w in "hello world".split()))

# Question 47
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
import ipaddress
try:
    ipaddress.IPv4Address("192.168.1.1")
    print(True)
except ipaddress.AddressValueError:
    print(False)

# Question 48
print("\nQuestion 48: Find all substrings of 'abc'")
s = "abc"
print([s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)])

# Question 49
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
import codecs
print(codecs.encode("hello world", "rot_13"))

# Question 50
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
def luhn(card):
    digits = [int(d) for d in str(card)]
    for i in range(len(digits)-2, -1, -2):
        d = digits[i] * 2
        if d > 9:
            d -= 9
        digits[i] = d
    return sum(digits) % 10 == 0
print(luhn("4532015112830366"))
