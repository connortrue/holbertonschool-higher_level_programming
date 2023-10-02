#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import json


class Base:
    """
    This class serves as the base class for all other classes in the project.
    It manages the 'id' attribute in all future classes, preventing code
    duplication.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the Base class.

        Parameters:
        id (int, optional): The id of the instance. If not provided, it will be
        incremented and assigned automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Parameters:
        list_dictionaries (list): A list of dictionaries.

        Returns:
        str: A JSON string that represents the list of dictionaries.

        Raises:
        TypeError: If list_dictionaries is not a list.
        """
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list")

        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Parameters:
        list_objs (list): A list of instances who inherits of Base.

        """
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(cls.__name__ + ".json", 'w') as file:
            file.write(cls.to_json_string(list_dicts))
