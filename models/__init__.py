#!/usr/bin/python3
"""
This module initializes the 'models' package by setting up the necessary 
components and ensuring that data storage and retrieval functionalities are
in place. It performs the following tasks:

1. Imports essential classes from various modules within the 'models' package:
   - BaseModel: The base class for all model classes.
   - User: Represents a user in the system.
   - State: Represents a state or region.
   - City: Represents a city, which is associated with a State.
   - Amenity: Represents a feature or service associated with a place.
   - Place: Represents a location or accommodation.
   - Review: Represents a review or rating given to a place.

2. Initializes an instance of FileStorage, a class responsible for
   managing file-based storage of model instances.

3. Loads existing data from storage into the system by invoking the 'reload'
   method on the FileStorage instance.

4. Retrieves all objects stored and stores them in a variable for further
   manipulation or access.

5. Defines a dictionary named 'classes' that maps class names (as strings) 
   to their corresponding class objects. This allows for dynamic access to 
   model classes based on string identifiers.

Attributes:
    storage (FileStorage): An instance of the FileStorage class for data 
                           persistence.
    loaded_objects (dict): A dictionary containing all objects currently
                           stored in the FileStorage instance.
    classes (dict): A dictionary mapping class names to class objects.
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Create an instance of FileStorage to handle data operations
storage = FileStorage()

# Load all previously saved objects from the file storage
storage.reload()

# Retrieve all objects from storage and store them in a variable
loaded_objects = storage.all()

# Define a dictionary to map class names to their respective classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}
