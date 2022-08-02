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
    

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
