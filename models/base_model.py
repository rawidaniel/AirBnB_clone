#! /usr/bin/python3
"""
    Defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
        Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize new BaseModel object
        """

        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.today()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                else:
                    if k == 'created_at' or k == 'updated_at':
                        self.__dict__[k] = datetime.strptime(v, t_format)
                    else:
                        self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
            Returns the string representation of this class
        """

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values
            of __dict__ of the instance
        """

        dict_rep = {}
        dict_rep['__class__'] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dict_rep[k] = v.isoformat()
            else:
                dict_rep[k] = v

        return dict_rep
