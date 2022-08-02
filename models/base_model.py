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
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def my_number(self):
        return self._my_number

    @my_number.setter
    def my_number(self, number):
        self._my_number = number
    

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
