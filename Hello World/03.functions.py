
# Basic
print("-" * 20 + "\n Basic \n" + "-" * 20)
def greet(first_name, last_name): # has parameters
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Kartheek", "Midde") # has arguments
greet("Virat", "Kohli")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Sachin Tendulkar")
print(message)

# Keyword Arguments
print("-" * 20 + "\n Keyword Arguments \n" + "-" * 20)
def increment(number, by):
    return number + by

print(increment(10, by=3)) 

# Optional Arguments
print("-" * 20 + "\n Optional Arguments \n" + "-" * 20)
def increment1(number, by=1): 
    return number + by

print(increment1(10))
print(increment1(10, 2))

# XArgs
print("-" * 20 + "\n XArgs \n" + "-" * 20)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

# XXArgs
print("-" * 20 + "\n XXArgs \n" + "-" * 20)
def save_user(**user): # can pass a dictionary
    print(user["id"])


save_user(id=1, name="John", age=22)


# Debugger
print("-" * 20 + "\n Debugger \n" + "-" * 20)
def multiply_nums(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total
    
print("Start")
print(multiply_nums(1, 2, 3))

# Exercise
print("-" * 20 + "\n Exercise \n" + "-" * 20)

def fizz_buzz(input):
    if (input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 == 0):
        return "Fizz"
    elif (input % 5 == 0):
        return "Buzz"
    return input

print(fizz_buzz(5))