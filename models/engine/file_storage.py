#!/usr/bin/python3


import json
from base_model import BaseModel

class FileStorage:
    def __FileStorage__(self):
        self.__FileStorage__ = FileStorage
    base_ptr = BaseModel
    json(to_dict(base_ptr))
    with open("base_ptr.json", "r+") as file:
        data = json.load