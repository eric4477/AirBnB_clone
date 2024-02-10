#!/usr/bin/python3
"""
module for the <User> class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    <User> class that inherits from
    <BaseModel> class and handle user
    information
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
