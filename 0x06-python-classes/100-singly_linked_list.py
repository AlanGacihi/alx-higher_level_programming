#!/usr/bin/python3

"""Singly-linked list"""


class Node:
    """Define a node"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
        data (int): The data of the new Node.
        next_node (Node): The next node of the new Node.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a singly-linked list"""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            new.next_node = temp.next_node
            while temp.next_node and value > temp.next_node.data:
                new.next_node = temp.next_node.next_node
                temp = temp.next_node
            temp.next_node = new

    def __str__(self):
        res = ""
        temp = self.__head
        while temp is not None:
            res = res + str(temp.data) + "\n"
            temp = temp.next_node
        res = res[:-1]
        return res
