#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Amenity_attribute_type(self):
        '''
            Test that Amenity class had name attribute's type.
        '''
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)

    def test_amenity_attr(self):
        '''
            Check if attribute exists
        '''
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "name"))
        self.assertTrue(hasattr(new_amenity, "place_amenities"))
        self.assertTrue(hasattr(new_amenity, "__tablename__"))

    def test_amenity_table(self):
        '''
           Check tablename
        '''
        new_amenity = Amenity()
        tablename = new_amenity.__tablename__
        self.assertEqual(tablename, "amenities")
