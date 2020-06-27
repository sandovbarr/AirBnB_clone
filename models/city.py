#!/usr/bin/python3
'''
    class for Cities
'''
from models.base_model import BaseModel


class City(BaseModel):
    ''' Class to assing name of the city '''
    state_id = ''
    name = ''
