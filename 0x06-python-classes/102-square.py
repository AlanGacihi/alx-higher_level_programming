#!/usr/bin/python3

"""Square"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
         Args:
         size (int): The size of the new square.
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if (self.__size != 0):
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#" * self.__size
                                    ))
        if (not self.__size):
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or type(value[1]) is not int or\
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        if (self.__size != 0):
            result = "\n" * self.__position[1]
            for i in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            result = result[:-1]
        if (not self.__size):
            result = ""
        return result

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ne__(self, other):
        return self.area() != other.area()
