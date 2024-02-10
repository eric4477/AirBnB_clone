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
    __file_path = "file.json"   # class attribute
    __objects = {}              # class attribute

    def all(self):
        """
        returns the dictionary of all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """adds the object obj with the key <obj class name>.id to
                the __objects dictionary.
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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as my_file:
            json.dump(obj_dict, my_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """

        try:
            if os.path.isfile(FileStorage.__file_path):  # if file exist
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    objs = json.load(f)  # load a dictionary form a file

                    for key, value in objs.items():
                        class_name, obj_id = key.split('.')
                        self.__objects[key] = eval(class_name)(**value)

        except Exception:  # if file note found do nothing
            return
