#!/usr/bin/python3
"""Doc"""


class Student:
    """
    Defines a student with first name, last name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class

        Parameters:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Parameters:
        attrs (list): A list of strings representing attribute names

        Returns:
        dict: A dictionary representation of the Student instance
        """

        if attrs is None:
            return {key: value for key, value in self.__dict__.items() if
                    isinstance(value, (list, dict, str, int, bool))}

        return {key: value for key, value in self.__dict__.items() if key in
                attrs and isinstance(value, (list, dict, str, int, bool))}
