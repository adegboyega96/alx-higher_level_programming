#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class module"""

    def __init__(self, first_name, last_name, age):
        """Initialize student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
