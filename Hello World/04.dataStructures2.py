from collections import deque
from array import array
from sys import getsizeof

# Stacks
print("-" * 20 + "\n Stacks \n" + "-" * 20)
browsing_session = [1, 2, 3, 4]
browsing_session.pop()  # removes top item from stack
browsing_session.append(5)  # adds a new item to stack
print(browsing_session[-1])  # shows the top item of the stack
if browsing_session:  # checks if stack is not empty
    print("redict to", browsing_session[-1])

if not browsing_session:
    print("redirect disabled")

# Queues
print("-" * 20 + "\n Queues \n" + "-" * 20)
queue = deque([])  # to make removing elements easier
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()  # to remove an item from the start
print(queue)

if not queue:
    print("queue is empty")


# Tuples
print("-" * 20 + "\n Tuples \n" + "-" * 20)
# Tuples are immuate and can not be change, add or remove elements once created
# Functions can remove multiple values as tuples
# used where we don't want to modify the values or the sequence

point = (1, 2)
pointA = 1, 2  # Python reads this as tuple
pointB = 1,  # Python reads this as tuple because of trailing ,
pointC = ()  # empty tuple

pointD = (1, 2) + (3, 4)  # merging two tuples
print(pointD)

pointE = (1, 2) * 3
print(pointE)

pointF = tuple([1, 2, 3])  # convert list to tuple
print(pointF)

pointG = tuple("Hello world")
print(pointG)

print(pointG[3])
print(pointG[0:3])

point = (1, 2)
x, y = point
print(x, y)

if "l" in pointG:
    print("l in tuple")


# Swapping
print("-" * 20 + "\n Swapping \n" + "-" * 20)
x = 10
y = 5

x, y = y, x  # since it is considered a tuple
x, y = (y, x)  # same as above - internally x, y = (5, 10)
a, b = 1, 2  # because of the above logic
print(x, y)

# Arrays
print("-" * 20 + "\n Arrays \n" + "-" * 20)
# Arrays take less memory and perform faster than lists
# Noticeable when size is more than 10,000
# Use to enhance performance
# Need to import from array modules
# Need to know typecode
numbers = array("i", [1, 2, 3, 4, 5, 6])
numbers.append(7)
numbers.append(10)
numbers.remove(2)
numbers.pop()
print(numbers)
print(numbers[3])
# numbers[1] = 2.0 - will throw an error. since same typecode should be used

# Sets
print("-" * 20 + "\n Sets \n" + "-" * 20)
# Unordered collection
numbers = [1, 1, 2, 3, 4, 5, 5, 6]
uniques = set(numbers)
print(uniques)

secondSet = {1, 2, 3}
secondSet.add(4)
secondSet.add(5)
secondSet.remove(2)

print(secondSet)
print(len(secondSet))

firstSet = {1, 6, 9}
print(firstSet | secondSet)  # get union of 2 sets
print(firstSet & secondSet)  # get intersection of 2 sets
print(firstSet - secondSet)  # get the difference
print(firstSet ^ secondSet)  # get xor of 2 sets
# firstSet[0] - error since it does not support indexing
if 1 in firstSet:
    print('in set')


# Dictionaries
print("-" * 20 + "\n Dictionaries \n" + "-" * 20)
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 3
print(point["x"])
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])  # will throw an error without check
print(point.get("a", 0))  # will return None if default 0 is not passed

del point["x"]  # to delete item from dict

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)


# Dictionary Comprehension
print("-" * 20 + "\n Dictionary Comprehension \n" + "-" * 20)
values1 = []
for x in range(5):
    values1.append(x * 2)
print(values1)

# List comprehension
values2 = [x * 2 for x in range(5)]
print(values2)

# Sets comprehension
values3 = {x * 2 for x in range(5)}
print(values3)

# Dictionary comprehension
values4 = {x: x * 2 for x in range(5)}
print(values4)

# Tuple comprehension - Uses Generator expressions
# Generator does not store everything in memory
# it generates on each iteartyion
values5 = (x * 2 for x in range(5))
print(values5)
for x in values5:
    print(x)

values6 = (x * 2 for x in range(1000))
print("gen size: ", getsizeof(values6))
# print(len(values6)) - will throw an error as items are not generated

values7 = [x * 2 for x in range(1000)]
print("list size: ", getsizeof(values7))


# Unpacking operator
print("-" * 20 + "\n Unpacking Operator \n" + "-" * 20)
numbers = [1, 2, 3]
print(*numbers)

values = range(5)
print(*values)

values = [*range(5), *"Hello World"]
print(values)


firstList = [1, 2]
secondList = [3, 4]
values = [*firstList, 1, *secondList, "Hello"]
print(values)
values = [*firstList, 1, *secondList, *"Hello"]
print(values)

dict1 = {"x": 1}
dict2 = {"x": 2, "y": 3}
# if same key, overwrites it with the latest one
combined = {**dict1, **dict2, "z": 1}
print(combined)

# Exercise
print("-" * 20 + "\n Exercise \n" + "-" * 20)
# find the most repeated character in string
sentence = "This is a common interview question"
char_freq = {}
maxCount = 0
for char in sentence:
    char_freq[char] = char_freq.get(char, 0) + 1
    maxCount = max(maxCount, char_freq[char])
print(maxCount)

# since sorted function does not know how to sort dictionary
print(sorted(char_freq.items()))
char_freq_sorted = sorted(
    char_freq.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_freq_sorted[0])
