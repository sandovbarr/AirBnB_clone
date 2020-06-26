#!/usr/bin/python3
''' defines all common attributes/methods for other classes '''
import uuid
import models
from datetime import datetime


class BaseModel:
    ''' defines all common attributes/methods for other classes '''
    def __init__(self, *args, **kwargs):
        ''' constructor '''
        if kwargs:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "created_at" in kwargs.keys():
                self.created_at = datetime.now()
            if "updated_at" in kwargs.keys():
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        '''
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        '''
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = {"__class__": __class__.__name__}
        new_dict.update(self.__dict__)
        new_dict['created_at'] = new_dict['created_at'].strftime(timeformat)
        new_dict['updated_at'] = new_dict['updated_at'].strftime(timeformat)
        return (new_dict)
