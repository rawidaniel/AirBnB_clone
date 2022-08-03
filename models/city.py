#! /usr/bin/python3
"""
    Define City class
"""
from .base_model import BaseModel


class City(BaseModel):
    """
        Represents a City
    """

    state_id = ''
    name = ''
