#!/usr/bin/python3
"""
Testing Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Represent TestReview class
    """

    def test_attributes(self):
        """
        test empty attributes
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes_update(self):
        """
        attributes update
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This place was amazing!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "This place was amazing!")

    def test_inheritance(self):
        """
        Test inheritance
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))


if __name__ == '__main__':
    unittest.main()
