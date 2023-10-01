#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here. Hi Travis."""


class Base:
    """
    This class serves as the base class for all other classes in the project.
    It manages the 'id' attribute in all future classes, preventing code duplication.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the Base class.

        Parameters:
        id (int, optional): The id of the instance. If not provided, it will be incremented
        and assigned automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
