#!/usr/bin/python3
''' Module for users creation '''
from models import *

class User(BaseModel):
	email = ""
	password = ""
	first_name = ""
	last_name = ""
