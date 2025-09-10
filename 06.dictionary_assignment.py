# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (SOLUTIONS)
# ==================================

# Question 1
students = {'John': 20, 'Alice': 22, 'Bob': 19}
print("Q1:", students)

# Question 2
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4
print("Q2:", d)

# Question 3
info = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Q3:", list(info.keys()))

# Question 4
langs = {'python': 3, 'java': 2, 'c++': 1}
print("Q4:", list(langs.values()))

# Question 5
person = {'name': 'Alice', 'age': 30, 'city': 'London'}
print("Q5:", 'age' in person)

# Question 6
temp_dict = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
temp_dict.pop('temp')
print("Q6:", temp_dict)

# Question 7
marks = {'math': 85, 'science': 92, 'english': 78}
print("Q7:", sum(marks.values()))

# Question 8
squares = {x: x**2 for x in range(1, 6)}
print("Q8:", squares)

# Question 9
text = "hello"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("Q9:", freq)

# Question 10
d1, d2 = {'a': 1, 'b': 2}, {'c': 3, 'd': 4}
d1.update(d2)
print("Q10:", d1)

# Question 11
nested = {'person': {'name': 'Alice', 'age': 25}}
print("Q11:", nested)

# Question 12
print("Q12:", nested['person']['name'])

# Question 13
d13 = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("Q13:", d13)

# Question 14
d13['fruits'].append('orange')
print("Q14:", d13)

# Question 15
coords = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("Q15:", coords)

# Question 16
print("Q16:", coords['coordinates'][0])

# Question 17
d17 = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("Q17:", d17)

# Question 18
d17['vowels'].add('o')
print("Q18:", d17)

# Question 19
d19 = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("Q19:", d19)

# Question 20
print("Q20:", d19['company']['department']['employee']['name'])

# Question 21
d21 = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("Q21:", d21)

# Question 22
print("Q22:", {k: type(v).__name__ for k, v in d21.items()})

# Question 23
funcs = {'len': len, 'str': str, 'int': int}
print("Q23:", funcs)

# Question 24
print("Q24:", {k: f("123") for k, f in funcs.items()})

# Question 25
ops = {'double': lambda x: x*2, 'square': lambda x: x**2}
print("Q25:", ops)

# Question 26
print("Q26:", {k: f(5) for k, f in ops.items()})

# Question 27
classes = {'list': list, 'dict': dict, 'set': set}
print("Q27:", classes)

# Question 28
print("Q28:", {k: v() for k, v in classes.items()})

# Question 29
d29 = {'a': None, 'b': None, 'c': None}
print("Q29:", d29)

# Question 30
d30 = {k: (0 if v is None else v) for k, v in d29.items()}
print("Q30:", d30)

# Question 31
d31 = {'is_active': True, 'is_admin': False}
print("Q31:", d31)

# Question 32
print("Q32:", sum(d31.values()))

# Question 33
d33 = {'z1': 3+4j, 'z2': 1+2j}
print("Q33:", d33)

# Question 34
print("Q34:", {k: abs(v) for k, v in d33.items()})

# Question 35
d35 = {'a': {'b': {'c': {'d': 100}}}}
print("Q35:", d35)

# Question 36
print("Q36:", d35['a']['b']['c']['d'])

# Question 37
d37 = {'r1': range(3), 'r2': range(5)}
print("Q37:", d37)

# Question 38
print("Q38:", {k: list(v) for k, v in d37.items()})

# Question 39
d39 = {'g1': (i for i in range(3))}
print("Q39:", d39)

# Question 40
print("Q40:", {k: list(v) for k, v in d39.items()})

# Question 41
d41 = {'it1': iter([1, 2, 3]), 'it2': iter('abc')}
print("Q41:", d41)

# Question 42
print("Q42:", {k: list(v) for k, v in d41.items()})

# Question 43
d43 = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("Q43:", d43)

# Question 44
print("Q44:", {k: sum(map(sum, v)) if isinstance(v[0], list) else sum(v) for k, v in d43.items()})

# Question 45
d45 = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("Q45:", d45)

# Question 46
print("Q46:", d45['config']['db']['port'])

# Question 47
d47 = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("Q47:", d47)

# Question 48
print("Q48:", d47['points'][0])

# Question 49
d49 = {'groups': [{1, 2, 3}, {4, 5, 6}], 'categories': [{'a', 'b'}, {'c', 'd'}]}
print("Q49:", d49)

# Question 50
all_sets = d49['groups'] + d49['categories']
union_all = set().union(*all_sets)
print("Q50:", union_all)
