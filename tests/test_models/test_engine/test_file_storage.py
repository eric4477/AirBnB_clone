#!/usr/bin/python3
""" model for testing file storage"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    represent fileStorage class
    """
    def setUp(self):
        """
        Create a test instance of FileStorage
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Delete the test file if it exists
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save_and_reload(self):
        """
        Create some test BaseModel objects
        """
        obj1 = BaseModel()
        obj2 = BaseModel()

        # Add the objects to the FileStorage instance
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Save the objects to file
        self.storage.save()

        # Reload the objects from file
        self.storage.reload()

        # Ensure objects are loaded back correctly
        loaded_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), loaded_objects)
        self.assertIn("BaseModel.{}".format(obj2.id), loaded_objects)
        self.assertIsInstance(loaded_objects["BaseModel.{}".format(
            obj1.id)], BaseModel)
        self.assertIsInstance(loaded_objects["BaseModel.{}".format(
            obj2.id)], BaseModel)


if __name__ == "__main__":
    unittest.main()
