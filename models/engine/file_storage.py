#!/usr/bin/python3
"""Convert the dictionary representation in python to a JSON string.
   and JSON to a dictionary representation
"""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances.
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
        <class name>.id (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        class_name = obj.__class__.__name__  # get the class name from object
        key = '{}.{}'.format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        all_obj = FileStorage.__objects
        obj_dict = {}
        # Convert 'BaseModel' to 'dict' by using to_dict() function
        for obj in all_obj.keys():
            obj_dict[obj] = all_obj[obj].to_dict()
        # open a file and save json str to it
        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(obj_dict, my_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        if os.path.isfile(FileStorage.__file_path):  # check if file path exist
            with open(FileStorage.__file_path, "r") as my_file:
                objs = json.load(my_file)  # load a dictionary form a file

                for values in objs.values():
                    # get the class name
                    cls_name = values["__class__"]
                    cls = eval(cls_name)
                    instance = cls(**values)

                    FileStorage.__objects['id'] = instance
