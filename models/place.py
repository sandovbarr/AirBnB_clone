#!/usr/bin/python3
'''
    class Amenity
'''
from models import *


class Place(BaseModel):
    ''' Class to assing name of the Amenity'''
    city_id: ""
    user_id: ""
    name = ""
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = float - 0.0
    amenity_ids = []
