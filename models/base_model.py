#!/usr/bin/python3
''' defines all common attributes/methods for other classes '''
import uuid
from datetime import datetime


class BaseModel:
    ''' defines all common attributes/methods for other classes '''
    def __init__(self, *args, **kwargs):
        ''' constructor '''
        if kwargs:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "created_at" in kwargs.keys():
                self.created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            if "updated_at" in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' returns str representation '''
        return "[{}] ({}) {}"\
            .format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
            updates the public instance attribute
            updated_at with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        '''
        return_dict = {"__class__": __class__.__name__}
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        #  self.created_at.isoformat()
        #  self.updated_at.isoformat()
        return_dict.update(self.__dict__)
        return (return_dict)
