#!/usr/bin/python3
"""
Defines unittests for models/city.py.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test for ammenity
    """

    def test_attributes(self):
        """
        test attributes
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attributes_update(self):
        """
        update attributes
        """
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        self.assertEqual(amenity.name, "Wi-Fi")

    def test_inheritance(self):
        """
        test inheritance
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
