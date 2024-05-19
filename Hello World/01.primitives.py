# pylint: disable=missing-module-docstring
# to prevent the pylint problem - missing module docstring

import math

# Variables
students_count = 1000
rating = 5.99
is_publised = False
course_name = "Python Programming"

# Strings
print("-" * 20 + "\n STRINGS \n" + "-" * 20)
long_message = """
Hi,
This is a long message.
"""

print(len(long_message))  # length of the string
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])  # end index excluded
print(course_name[0:])  # everything from start index
print(course_name[:4])  # everything till the last index - excluded
print(course_name[:])  # returns a copy of the original string

# Escape characters
# \\
# \"
# \'
# \n - new line
course_escape_name = "Python \"Programming\""  # escaping certain characters
print(course_escape_name)

# Formatted string
first_name = "Kartheek"
last_name = "Midde"
name = f"{first_name} {last_name}"  # string will be evaluated
print(name)
# any valid expressions can be put
length = f"{len(first_name) + len(last_name)}"
print(length)


# String functions
print("-" * 20 + "\n String functions \n" + "-" * 20)

course = "  Python learning  "
print(course.upper())  # original string is not affected
print(course)
print(course.lower())
print(course.title())  # capital of first in every word
print(course.strip())  # trims white spaces at the ends of the string
print(course.lstrip())  # strip from left
print(course.rstrip())  # strip from right


print("-" * 20 + "\n Find/Replace/Existence \n" + "-" * 20)
print(course.find("lear"))  # find the character(s) in the string
print(course.find("t"))
print(course.replace("n", "j"))
print(course)
print("pro" in course)  # returns boolean
print("Pro" in course)
print("Car" not in course)


# Numbers
print("-" * 20 + "\n NUMBERS \n" + "-" * 20)
x = 1
y = 2.3
z = 1 + 2j  # complex numbers

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # quotient
print(10 // 3)  # integer quotient
print(10 % 3)  # reminder
print(10 ** 3)

print("-" * 20 + "\n Number functions \n" + "-" * 20)
print(round(2.99))
print(abs(-2.9))
# import modules when required
print(math.ceil(2.3))

# Type conversion
x = input("x: ")  # returns a string
y = int(x) + 10
print(f"x is {x}, y is {y}")
