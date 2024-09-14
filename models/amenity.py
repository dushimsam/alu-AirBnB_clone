#!/usr/bin/python3
"""
Create Amenity module inheriting properties from the BaseModel Class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is the amenity class

    Attributes:
        name (str): The name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
