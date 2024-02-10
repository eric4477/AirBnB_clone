#!/usr/bin/python3
"""
state testing
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    TestState class
    """

    def test_attributes(self):
        """
        empty attributes
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes_update(self):
        """
        test_attributes_update
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_inheritance(self):
        """
        test inheritance
        """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))


if __name__ == '__main__':
    unittest.main()
