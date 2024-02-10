#!/usr/bin/python3
"""
Defines unittests for models/city.py.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    unit test for city class
    """

    def test_attributes(self):
        """
        test attributes
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes_update(self):
        """
        test attributes update
        """
        city = City()
        city.state_id = "CA"
        city.name = "Los Angeles"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "Los Angeles")

    def test_inheritance(self):
        """
        test inheritance
        """
        city = City()
        self.assertTrue(isinstance(city, BaseModel))


if __name__ == "__main__":
    unittest.main()
