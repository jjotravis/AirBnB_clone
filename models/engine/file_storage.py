#!/usr/bin/python3
import json
import os


class FileStorage():
    """
    File Storage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Sets in obects dictionary the obj key
        with <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes obj dict to a json file
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the SON file to __objects(dictionary),
        then into an instance
        """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, mode="r", encoding="utf-8") as f:
                    read_file = f.read()
                    # list of instances containing a list of dicts
                    list_of_instances = json.loads(read_file)
                    self.__objects = list_of_instances
            else:
                pass

        except FileNotFoundError as e:
            return e
