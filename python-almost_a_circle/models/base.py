#!/usr/bin/python3
"""Base Class"""
import json
from os.path import exists


class Base:
    """_summary_
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor

        Args:
            id (int): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the Json  str representation of list_dictionary"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""
        if not list_objs:
            list_objs = []

        my_list = []
        for obj in list_objs:
            my_list.append(obj.to_dictionary())

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """return deserialized json_string"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        dummy = cls(3, 5)
        dummy.x = 0
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file containing JSON string
        representation of a class 'cls' object"""
        filename = f"{cls.__name__}.json"

        if not exists(filename):
            return []
        with open(filename, "r") as f:
            json_str = f.read()
            json_list = cls.from_json_string(json_str)
            list_objs = []
            for dict in json_list:
                list_objs.append(cls.create(**dict))
            return list_objs
