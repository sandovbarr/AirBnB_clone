#!/usr/bin/python3
'''
    class for States
'''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Class to assing review '''
    place_id = ''
    user_id = ''
    text = ""
