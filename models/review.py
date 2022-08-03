#! /usr/bin/python3
"""
    Define review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
        Represents a review
    """

    place_id = ''
    user_id = ''
    text = ''
