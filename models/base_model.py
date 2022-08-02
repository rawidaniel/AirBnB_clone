#!/usr/bin/python3

import uuid
import unittest
import sys
import os

""" This program will declare a class called BaseModel which takes user name, number. And it will generate unique uuid to identify ... """

class BaseMode():
    def __init__(self, *args, **kwargs):
        ''' here i will generate unique id'''
        ...

    def __str__(self):
        return f"[BaseModel]"

    @property
    def name(self):
        return self._name

    @setter.name
    def name(self, name):
        self._name = name

    @property
    def my_number(self):
        return self._my_number

    @setter.my_number
    def my_number(self, number):
        self._my_number = number

