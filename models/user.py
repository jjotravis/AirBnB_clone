#!/usr/bin/python3
"""
Defining a class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for mangaging user objects
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
