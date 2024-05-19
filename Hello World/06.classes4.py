# Inheritance
print("-" * 20 + "\n Inheritance \n" + "-" * 20)


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    # method overriding
    def __init__(self):
        super().__init__()  # can be called after other setters
        self.weight = 5

    def walk(self):
        print("walk")


class Fish(Animal):
    def eat(self):
        print("eat")


mammal = Mammal()
mammal.eat()
mammal.walk()

# Instance or subclass
print("-" * 20 + "\n Instance or subclass \n" + "-" * 20)
print(isinstance(mammal, Mammal))
print(isinstance(mammal, Animal))
print(isinstance(mammal, object))  # object is the base parent class
print(issubclass(Mammal, Animal))

# Overriding
print("-" * 20 + "\n Overriding \n" + "-" * 20)
print(mammal.age)  # will throw an error without super() as method is overridden
print(mammal.weight)
