#!/usr/bin/python3
""" tests for User class"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    represent a test
    """

    def test_user_attributes(self):
        """
        test attributes
        """
        # create a new instance of User
        user = User()
        # checking if the default first_name attribute is an empty string
        self.assertEqual(user.first_name, "")
        # checking if the default last_name attribute is an empty string
        self.assertEqual(user.last_name, "")
        # checking if the default email attribute is an empty string
        self.assertEqual(user.email, "")
        # checking if the default password attribute is an empty string
        self.assertEqual(user.password, "")

    def test_user_inherits_from_base_model(self):
        """
        test inherits
        """
        # create a new instance of User
        user = User()
        # checking if the user class is a subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

    def test_usr_str_representation(self):
        """
        test user string reprsentation
        """
        # create a new instance of User
        user = User()
        # set the attributes for the User instance attributes
        user.first_name = "Mark"
        user.last_name = "Johnson"
        user.email = "mark@example.com"
        user.password = "mark123"
        #  get the User instance string representation
        user_str = str(user)
        # check if the <User> is in the string representation
        self.assertIn("User", user_str)
        # check if the first name is in the string representation
        self.assertIn("Mark", user_str)
        # check if the last name is in the string representation
        self.assertIn("Johnson", user_str)
        # check if the email is in the string representation
        self.assertIn("mark@example.com", user_str)
        # check if the password is in the string representation
        self.assertIn("mark123", user_str)


if __name__ == "__main__":
    unittest.main()
