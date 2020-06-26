#!usr/bin/python3
'''
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''
import json

class FileStorage: 
	
    def __init__(self, file_path, objects):
        ''' constructor '''
        self.file_path
        self.objects

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
		self.objects.update(obj.__class__.__name__)

	def save(self):
		'''
            save information of object in file JSON        
		'''
		with open(__file_path, mode='w', encoding='utf-8') as file:
			file.write(json.dumps(__file_path))

	def reload(self): 
