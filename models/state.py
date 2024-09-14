#!/usr/bin/python3
"""
The class definition for the BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    The class definition
    
    Attributes:
        name (str): The state name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.name = State.name
