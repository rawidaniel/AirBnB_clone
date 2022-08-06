#!/usr/bin/python3
""" Test cases for BaseModel """
import re
import cmd
import os
import json
import time
import unittest
import uuid
import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime



class TestBaseModel(unittest.TestCase):
    """ Class to test BaseModel features """

    def SetUp(self):
        """ Any set up variables go here """
        pass

    def resetStorage(self):
        """ Reset the storage file """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """ Check type of instance created """
        b = BaseModel()
        self.assertEqual(str(type(b)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_instance_kwargs(self):
        """ Test instantiation with kwargs"""
        b = BaseModel()
        b.name = "scoot"
        b.age = 98
        model_json = b.to_dict()
        new_model = BaseModel(**model_json)
        self.assertEqual(new_model.to_dict(), b.to_dict())

    def test_instance_dict(self):
        """ Test instantiation with a dict """
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(42, 12, 6, 12, 54, 6, 12).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "char": "a",
             "str": "string time",
             "int": 42,
             "float": 3.14}
        base = BaseModel(**d)
        self.assertEqual(base.to_dict(), d)

    def test_no_arg_init(self):
        """ Test insantiation with no args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.__init__()

    def test_many_arg_init(self):
        """ Test instantiation with many args """
        self.resetStorage()
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_attributes(self):
        """ Test if attributes are equal to default type """
        attrs = storage.attributes()["BaseModel"]
        b = BaseModel()
        for k, v in attrs.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)

    def test_none(self):
        """ Test that basemodel is not none """
        b = BaseModel()
        self.assertIsNotNone(b)

    def test_str_model(self):
        """ Test if group 1 exists and is of type BaseModel """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        self.assertEqual(reb.group(1), "BaseModel")

    def test_str_id(self):
        """ Test if group 2 exists and is of type id """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        self.assertEqual(reb.group(2), b.id)

    def test_str_datetime(self):
        """ Test if datetime matches with group 3 """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        date = reb.group(3)
        date = re.match("(datetime\.datetime\(*\))", date)

    def test_to_dict_no_args(self):
        """ Test to_dict function without args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.to_dict()

    def test_to_dict_many_args(self):
        """ Test to_dict function with many args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.to_dict(98, 99)

    def test_to_dict_name(self):
        """ Test if name is implemented into BaseModel """
        b = BaseModel()
        b.name = "scoot"
        d = b.to_dict()
        self.assertEqual(d["name"], b.name)

    def test_to_dict_class(self):
        """ Test if class is of type BaseModel """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["__class__"], type(b).__name__)

    def test_to_dict_age(self):
        """ Test if age is implemented into BaseModel """
        b = BaseModel()
        b.age = 108
        d = b.to_dict()
        self.assertEqual(d["age"], b.age)

    def test_to_dict_id(self):
        """ Test if id is implemented into BaseModel """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)

    def test_uniq_id(self):
        """ Testing uniquesness of id """
        list_comp = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(list_comp), len(set(list_comp)))

    def test_to_dict_created_at(self):
        """ Test if created_at is implemented into BaseModel """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["created_at"], b.created_at.isoformat())

    def test_to_dict_updated_at(self):
        """ Test if updated_at is implemented into BaseModel """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())

    def test_save_no_args(self):
        """ Test save against no argument """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_save_many_args(self):
        """ Test save with too many arguments """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.save(4, 42)

    def test_string_model(self):
        """ testing that model string matched output """
        george = BaseModel()
        string = "[BaseModel] ({}) {}".format(george.id, george.__dict__)
        self.assertEqual(george.__str__(), string)

if __name__ == '__main__':
    unittest.main()
