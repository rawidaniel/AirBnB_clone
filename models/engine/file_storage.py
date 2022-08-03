#! /usr/bin/python3
"""
    Defines the FileStorage class
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """
        A class that serializes instances to a JSON file and
        deserializes JSON file to instances

        Attributes:
            __file_path (str)
            __objects (dict)
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """
            Initialize a new instance
        """
        pass

    def all(self):
        """
            Returns the dictionary
        """

        return FileStorage.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id
        """

        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
            Serializes __objects to the JSON file (path: __file_path)
        """

        dict_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict_obj, f)

    def reload(self):
        """
            Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """

        try:
            with open(FileStorage.__file_path, 'r') as f:
                for v in json.load(f).values():
                    class_name = v['__class__']
                    del v['__class__']
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass
