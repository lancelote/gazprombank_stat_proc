"""
main.py testing
"""

import unittest
import os
from app.main import get_files, unzip

# Test bank statements directory
DIR = "test/test_data/test_statements"


class TestGetFiles(unittest.TestCase):
    """
    Test get_files() function
    """

    def setUp(self):
        """
        Setup file list of zipped files
        """
        self.file_list = get_files(DIR)

    def test_get_files_works_correct(self):
        """
        Test if the given file in the list
        """
        for file in ["w00633066A22.zip",
                     "w00633066A22.zip",
                     "w00633066952.zip"]:
            self.assertIn(file, self.file_list)


class TestUnzip(unittest.TestCase):
    """
    Test unzip function
    """

    def setUp(self):
        """
        Unzip files and create a list of them
        """
        for file in get_files(DIR):
            unzip(file, DIR)
        self.unzipped_file_list = get_files(os.path.join(DIR, "unzipped"))

    def test_unzip_works_correct(self):
        """
        Test if given file in the list of unzipped files
        """
        for file in ["w00633066A22.txt",
                     "w006330661M2.txt",
                     "w00633066952.txt"]:
            self.assertIn(file, self.unzipped_file_list)
