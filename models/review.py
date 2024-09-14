#!/usr/bin/python3
"""
the Review class module inheriting the properties from the BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The class definition
    Properties:
        place_id (str): The place id
        user_id (str): The user id
        text (str): The text of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
