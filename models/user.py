#! /usr/bin/python3
"""
    Define User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
        Represents a user
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
