#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """_summary_
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dic repr of a student instance.

        Returns:
            _type_: _description_
        """
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr, value in self.__dict__.items():
            if attr in attrs:
                student_dict[attr] = value

        return student_dict

    def reload_from_json(self, json):
        """_Replace all attributes of the Student instance

        Args:
            json (_type_): _description_
        """
        for attr, value in json.items():
            setattr(self, attr, value)
