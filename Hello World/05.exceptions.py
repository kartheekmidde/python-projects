from timeit import timeit  # to calculate execution time of a code

# Exceptions
print("-" * 20 + "\n Exceptions \n" + "-" * 20)
try:
    file = open("01.primitives.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close() # may not execute when exception occurs
except (ValueError, ZeroDivisionError) as ex:
    print("You did not enter a valid age. ")
    print(ex)
    print(type(ex))
except FileNotFoundError as ex:
    print("File not found")
else:  # will be executed when no exceptions are thrown
    print("Else is executed when no exceptions thrown")
finally:
    print("finally will always be executed")
    # file.close()


# With statement
# To automatically release external resources - similar to above
print("-" * 20 + "\n With statement \n" + "-" * 20)
try:
    with open("app.py") as file:
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close() # may not execute when exception occurs
except (ValueError, ZeroDivisionError) as ex:
    print("You did not enter a valid age. ")
except FileNotFoundError as ex:
    print("File not found")
else:  # will be executed when no exceptions are thrown
    print("No exceptions thrown")


# Raising exceptions
print("-" * 20 + "\n Raising Exceptions \n" + "-" * 20)


def calcuate_xfactor(age):
    if (age <= 0):
        raise ValueError("Age can not be zero or less")
    return 10/age


try:
    calcuate_xfactor(0)
except ValueError as ex:
    print(ex)


# Cost of raising exceptions
print("-" * 20 + "\n Cost of raising Exceptions \n" + "-" * 20)

code1 = """
def calcuate_xfactor(age):
    if (age <= 0):
        raise ValueError("Age can not be zero or less")
    return 10/age


try:
    calcuate_xfactor(0)
except ValueError as ex:
    pass
"""

print("first code", timeit(code1, number=10000))

code2 = """
def calcuate_xfactor(age):
    if (age <= 0):
        return None
    return 10/age


xfactor = calcuate_xfactor(0)
if xfactor == None:
    pass # You can pass the statement when we don't need to execute anything
"""

print("first code", timeit(code2, number=10000))
