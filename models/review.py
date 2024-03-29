#!/usr/bin/python3
"""Module defining the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class to represent reviews.
    Class Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who created the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
