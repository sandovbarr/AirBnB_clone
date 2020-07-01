#!/usr/bin/python3
"""File Storage Unit Tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models
import os
import sys
import pep8
import unittest


class TestFileStorage(unittest.TestCase):
    """Test cases for class FileStorage"""

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def setUp(self):
        """Sets up the testing environment to not change the
        previous file storage
        """
        self.file_path = models.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, 'file.json')

    def tearDown(self):
        """Removes the JSON file after test cases run """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists('file.json'):
            os.rename('file.json', self.file_path)

    def test_instantiation(self):
        """Tests for proper instantiation"""
        insta_storage = FileStorage()
        self.assertIsInstance(insta_storage, FileStorage)

    def test_all(self):
        """Tests all """
        insta_storage = FileStorage()
        insta_dict = insta_storage.all()
        self.assertIsNotNone(insta_dict)
        self.assertEqual(type(insta_dict), dict)

    def test_save(self):
        """Tests save """
        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_new(self):
        """Tests the new method"""
        insta_storage = FileStorage()
        insta_dict = insta_storage.all()
        B1 = User()
        B1.id = '777'
        B1.name = "B1"
        insta_storage.new(B1)
        key = type(B1).__name__ + '.' + B1.id
        self.assertIsNotNone(insta_dict[key])

    def test_reload(self):
        """Tests for the reload method"""
        insta_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for item in f:
                self.assertEqual(item, "{}")
        self.assertIs(insta_storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
