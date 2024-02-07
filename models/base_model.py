#!/usr/bin/python3
"""
BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):  # updated T-5
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)  # for task 5

    def __str__(self):
        """
        Returns:
        str: A formatted string representing the object's state or information.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Method for updating the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save() # storage: is a FileStorge instance

    def to_dict(self):
        """
        Method for copying the class name, created_at, updated_at as keys
        from the instance __dict__ and returning the copied __dict__.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
