from abc import ABC, abstractmethod

# Inheritance
print("-" * 20 + "\n Inheritance \n" + "-" * 20)


class InvalidOperationException(Exception):
    pass


# make the class abstract
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationException("Stream is already open")
        self.opened = True
        print("Stream is opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationException("Stream is already closed")
        self.opened = False
        print("Stream is closed")

    # to make the method abstract method
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network")


# can not instantiate abstract class steam. Only inherited classes can be instantiated
# stream = Stream()
stream = FileStream()
stream.open()
stream.read()
stream.close()
