#!/usr/bin/python3
""" This contains a class that serializes and deserializes 
    instances into JSON files and vicev-versa """
import json


class FileStorage:
    """ This class serializes and deserializes JSON file to instances
        and vice versa """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary objects """
        return FileStorage.__objects___

    def new(self, obj):
        """ sets in __objects the obj with key """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file
            (path: __file_path) """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """ delete obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """ call reload() method for deserializing the JSON file to objects """
        self.reload()

