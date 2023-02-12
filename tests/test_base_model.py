#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the base Model Class"""
    def test_if_args_is_instance(self):
        # Checks if BaseModel is same type as the instance BaseModel
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_a_public_str(self):
        # check if id attribute is a str
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        # checks if created is datetime
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        # checks if updated at is datetime
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_models(self):
        # checks if two instances have different ids
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)




if __name__ == "__main__":
    unittest.main
