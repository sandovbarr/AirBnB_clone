#!/usr/bin/python3
'''
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''
import json

class FileStorage:

    def __init__(self, file_path, objects):
        ''' constructor '''
        self.file_path = "file.json"
        self.objects = {}

	@property
    def file_path(self):
        ''' getter '''
        return self.__file_path

	@property
	def objects(self):
        ''' getter '''
		return self.__objects

    @file_path.setter
    def file_path(self, value):
        ''' setter '''
		if type(value) == str:
			self.__file_path = value

	@objects.setter
	def objects(self, value={}):
        ''' setter '''
		self.__objects = value

	def all(self):
        ''' returns the dictionary __objects '''
		return self.objects

	def new(self, obj):
        '''
            sets in __objects the obj with
            key <obj class name>.id
        '''
		self.objects[str(obj.__class__.__name__, + ',' + obj.id)] = obj

	def save(self):
		'''
            save information of object in file JSON
		'''
		with open(__file_path, mode='w', encoding='utf-8') as file:
			file.write(json.dumps(__file_path))

	def reload(self):
        '''
            load information of object in file JSON
		'''
        if __file_path:
            with open(__file_path, mode='r', encoding='utf-8') as file:
                self.objects = json.loads(__file_path)

from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)