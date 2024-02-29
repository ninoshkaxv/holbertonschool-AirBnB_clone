#!/usr/bin/python3
"""
Class BaseModel
"""
from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage
import models


class BaseModel:
    """
    Base class for the Airbnb project with the principal funtion to inherit
    """
    def __init__(self, *args, **kwargs):
        """
        Initialises a BaseModel instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        Returns the string of a BaseModel instance
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Changes the updated_at time of an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict
