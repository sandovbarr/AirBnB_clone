#!usr/bin/python3
'''
    import all modules
'''
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

__all__ = ['BaseModel', 'FileStorage', 'User']