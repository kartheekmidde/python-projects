# Lists
print("-" * 20 + "\n Lists \n" + "-" * 20)

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 1]]
zeros = [0] * 20
print(zeros)
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)
print(len(chars)) # length of the list

# Accessing list items
print("-" * 20 + "\n Accessing List items \n" + "-" * 20)
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0: 3])
print(letters[-1])
print(letters[1:])
print(letters)
print(letters[:]) # copy of the list
print(letters[::2]) # print only second element in the list START:STOP:STEP
print(numbers[2:20:3]) # start at 2, end at 19, jump to every third element
print(numbers[::2])
print(numbers[::-1]) # print in reverse order


# Unpacking lists
print("-" * 20 + "\n Unpacking list \n" + "-" * 20)
numbers = [1, 2, 3]
first, second, third = numbers
print(first)
print(second)
print(third)

firstN, secondN, *otherN = [1, 2, 3, 4, 5, 6, 7]
print(firstN)
print(otherN)

firstL, *otherL, lastL = list(range(20))
print(firstL)
print(lastL)


# Looping over lists
print("-" * 20 + "\n Looping over lists \n" + "-" * 20)
letters = ["a", "b", "c"]
for index, letter in enumerate(letters): # if we need index as well - returns tuple
    print(index, letter)


# Adding/removing from list
print("-" * 20 + "\n Adding or removing from list \n" + "-" * 20)
letters = ["a", "b", "c", "d", "e", "d", "f"]
letters.append("d") # adds at the end
print(letters)
letters.insert(0, "-")
print(letters)


letters.pop() # removing from the end
print(letters)
letters.pop(1) # remove at an index
print(letters)
letters.remove("b") # remove an element (first appearance) if index is not known
print(letters) 
# del letters[0] # remove an item at index
# print(letters)
del letters[1:3] #remove items in the range excluded
print(letters)
letters.clear() # remove all items from the list
print(letters)


# Finding from list
print("-" * 20 + "\n Finding from list \n" + "-" * 20)
chars = ["a", "b", "c"]
print(chars.index("a"))
if "d" in chars:
    print(chars.index("d"))

print(letters.count("a")) # number of apperances 


# Sorting list
print("-" * 20 + "\n Sorting list \n" + "-" * 20)
numbers = [3, 9, 0, 12, 1, 2]
numbers.sort() # updates original list
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers)) # returns a new sorted list
print(sorted(numbers, reverse=True))
print(numbers)


# Sorting tuple
print("-" * 20 + "\n Sorting tuple \n" + "-" * 20)
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
items.sort() # can't sort tuple directly
print(items)

def sort_items(item):
    return item[1]

items.sort(key=sort_items)
print(items)


# Lambda function
print("-" * 20 + "\n Lambda/Sort function \n" + "-" * 20)
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# key=lambda parameters:expression
products.sort(key=lambda product:product[1])
print(products)

# Map function
print("-" * 20 + "\n Map function \n" + "-" * 20)
prices = list(map(lambda product:product[1], products)) # create map from the products, create list from iterable map
# for item in x:
    # print(item)  

print(prices)


# Filter function
print("-" * 20 + "\n Filter function \n" + "-" * 20)
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filterdProducts = list(filter(lambda product:product[1] >= 10, items))
# for prod in filterdProducts:
    # print(prod)
print(filterdProducts)


# List comprehension
print("-" * 20 + "\n List Comprehension \n" + "-" * 20)
# [expression for item in items] - apply expression for each item
# same as list(map(lambda product:product[1], products))
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
prices = [item[1] for item in items]
print(prices)
filtered = [item for item in items if item[1] >= 10]
print(filtered)


# Zip functions
print("-" * 20 + "\n Zip function \n" + "-" * 20)
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list(zip("abc", list1, list2)))