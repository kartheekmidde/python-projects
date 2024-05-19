# Properties
print("-" * 20 + "\n Properties \n" + "-" * 20)


class Product:
    def __init__(self, price):
        self.__price = price
        # self.set_price(price)
        # self.__price = price

    # @property annotation to make this method the getter for the property price
    # the name of the method should be the property name
    # these annotation hide the methods from outside
    @property
    def price(self):
        return self.__price

    # annotation to make this method the setter for the property price
    # without setter, the property is a read-only property
    # the name of the method should be the property name
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value

    # # to make it look like a property from outside of the class
    # price = property(get_price, set_price)


product = Product(50)
product.price = 10
print(product.price)
