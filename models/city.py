#!/usr/bin/python3
"""
The class module for the City class inheriting properties from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The class definition
    Properties:
        state_id (str): The state id
        name (str): The name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
