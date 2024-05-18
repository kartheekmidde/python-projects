
print("-" * 20 + "\n Conditional Statement \n" + "-" * 20)
temperatute = 15

if temperatute > 30:
    print("It is warm")
    print("Drink water")
elif temperatute > 20:
    print("It is nice")
else:
    print("It is cold")
print("Done") 


# Ternary operator
print("-" * 20 + "\n Ternary Operator \n" + "-" * 20)
age = 15
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical operator
print("-" * 20 + "\n Logical Operator \n" + "-" * 20)
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

print("-" * 20 + "\n Chaining Operators \n" + "-" * 20)
age = 22
if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")


# For Loops
print("-" * 20 + "\n For Loops \n" + "-" * 20)
# range(3) from 0 to 2
# range(1, 4) from 1 to 3 and 4 excluded
# range(1, 10, 2) step is 2 from 1 to 10, as long as it is below 10 - 10 excluded
for number in range(1, 9, 2): # 
    print("Attempt", number, number * ".")

# For Else (break else)
print("-" * 20 + "\n For Else \n" + "-" * 20)
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else: # control comes in when it does not break
    print("Attempted 3 times and failed")


# Nested loops
print("-" * 20 + "\n Nested Loops \n" + "-" * 20)
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")


# Iterables
print("-" * 20 + "\n Iterable \n" + "-" * 20)
n = 5
print(type(5))
print(type(range(5)))
# range object is iterable 
# strings are iterable
# lists are iterable

for x in "Python":
    print(x)

for x in [1, 2, 3]:
    print(x)

# While loops
print("-" * 20 + "\n While loops \n" + "-" * 20)

number = 100
while number > 0:
    print(number)
    number //= 2
    
command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# Infinite loops
print("-" * 20 + "\n Infinite loops \n" + "-" * 20)

# while True:
#     command = input(">")
#     print("Echo", command)
#     if command.lower() == "quit":
#         break

# QUIZ
print("-" * 20 + "\n QUIZ \n" + "-" * 20)
count = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        count +=1 
print(f"We have {count} event numbers")
