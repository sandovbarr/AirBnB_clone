#!/usr/bin/python3
''' file storage unittesting '''

import os
import unittest
import pep8
import json
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    ''' class for test methods in file storage class'''

    def test_pep8(self):
        """ Test that test/models/engine/file_storage.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        path = 'tests/test_models/test_engine/test_file_storage.py'
        r = pep8style.check_files([path])
        self.assertEqual(r.total_errors, 0, "Fix Your PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0, "Fix Your PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(file_storage.__doc__) >= 1)


class TestFunctions(unittest.TestCase):
    ''' functions unittesting '''

    def test_new_all_modules(self):
        storage = FileStorage()
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        key = str(my_model.__class__.__name__) + '.' + str(my_model.id)
        self.assertTrue(key in all_objs.keys())

    def save_module(self):
        """check save_to_file"""
        exists = os.path.exists('file.json')
        self.assertTrue(exists, True)

    def test_reload_method(self):
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs.keys()) > 0)
