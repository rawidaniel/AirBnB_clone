#!/usr/bin/python3

import uuid
import unittest
import sys
import os
import re
import datetime

""" This program will declare a class called BaseModel which takes user name, number. And it will generate unique uuid to identify ... """


class BaseModel:
    def __init__(self, *args, **kwargs):
        # here i will generate unique id
        """ args - postional argument --
            kwargs - named arguments -- 
            if nothing is given

            TO BE DONE
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()




    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def name(self, name):
        self.name = name

    def my_number(self, number):
        self.my_number = number

    def save(self):
        """ updates the update time with now"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """It organize __str__ into a dictionary"""
        """org_dict = dict()
        org_dict = {k: self.dict[k] for k in self.dict}
        org_dict["__class__"] = type(self).__name__ 
        #org_dict[""]
        return org_dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
    


