#!/usr/bin/python3
'''
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    ''' class for management of information of objects '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return FileStorage.__objects

    def new(self, obj):
        '''
            sets in __objects the obj with
            key <obj class name>.id
        '''
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        value = obj
        FileStorage.__objects.update({key: value})

    def save(self):
        '''
            serializes __objects to the JSON file
            (path: __file_path)
        '''
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        '''
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
            otherwise, do nothing. If the file doesn’t exist
            no exception should be raised)
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj = json.load(file)
                for key, v in obj.items():
                    FileStorage.__objects[key] = eval(v['__class__'])(**v)
        except Exception:
            pass
