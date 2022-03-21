#1/usr/bin/python3
"""  This creates the base model class """
import models
import uuid
from datetime import datetime



class BaseModel:
    """ BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """ Instantiates the instances of the class BaseModel """
        time_structure = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs != 0 and len(kwargs) != 0:
            for key, value in kwargs.items(time_fomr):
                if key== "updated_at":
                    self.updated_at = datetime.strptime(value, time_structure)
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, time_structure)
                elif key != "__class__":
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the base model """

        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
    


    
