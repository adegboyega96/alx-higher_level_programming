#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class module"""

    def __init__(self, first_name, last_name, age):
        """Initialize student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
