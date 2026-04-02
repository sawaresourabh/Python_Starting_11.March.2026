# Date : 11 March 2026 (just a trial to check that if the copied code is working or not)

# Python Data Structures for Beginners
# This file demonstrates basic data structures in Python

# 1. Lists - Ordered, mutable collections
print("=== LISTS ===")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Accessing elements (indexing starts at 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying elements
fruits[1] = "blueberry"
print("After modification:", fruits)

# List length
print("Number of fruits:", len(fruits))

print()

# 2. Tuples - Ordered, immutable collections
print("=== TUPLES ===")
coordinates = (10, 20, 30)
print("Coordinates tuple:", coordinates)

# Accessing elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Tuples cannot be modified (immutable)
# coordinates[0] = 15  # This would cause an error

print()

# 3. Dictionaries - Key-value pairs (unordered in older Python, ordered in Python 3.7+)
print("=== DICTIONARIES ===")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Student dictionary:", student)

# Accessing values by key
print("Student name:", student["name"])

# Adding new key-value pairs
student["major"] = "Computer Science"
print("After adding major:", student)

# Modifying values
student["age"] = 21
print("After updating age:", student)

print()

# 4. Sets - Unordered collections of unique elements
print("=== SETS ===")
numbers = {1, 2, 3, 4, 5, 2, 3}  # Duplicates are automatically removed
print("Numbers set:", numbers)

# Adding elements
numbers.add(6)
print("After adding 6:", numbers)

# Sets automatically handle uniqueness
numbers.add(3)  # Adding duplicate
print("After adding duplicate 3:", numbers)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Set1:", set1)
print("Set2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)

print()

# 5. Strings - Sequence of characters (technically a data structure)
print("=== STRINGS ===")
message = "Hello, World!"
print("Message:", message)

# String indexing
print("First character:", message[0])
print("Last character:", message[-1])

# String slicing
print("First 5 characters:", message[:5])
print("Characters from index 7:", message[7:])

# String methods
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Length:", len(message))

print()

# 6. Basic operations combining data structures
print("=== COMBINING DATA STRUCTURES ===")

# List of dictionaries
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19}
]
print("Students list:", students)

# Dictionary with lists as values
class_grades = {
    "math": [85, 92, 78],
    "science": [88, 95, 82],
    "english": [90, 87, 93]
}
print("Class grades:", class_grades)

# Accessing nested data
print("Alice's age:", students[0]["age"])
print("Math grades:", class_grades["math"])
print("First math grade:", class_grades["math"][0])