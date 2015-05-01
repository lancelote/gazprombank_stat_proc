import unittest
import os
from app.main import get_files, unzip

# Directory with test bank statements
directory = "test/test_data/test_statements"


class TestGetFiles(unittest.TestCase):

    def setUp(self):
        self.file_list = get_files(directory)

    def test_get_files_returns_correct_list(self):
        self.assertIn("w00633066A22.zip", self.file_list)
        self.assertIn("w006330661M2.zip", self.file_list)
        self.assertIn("w00633066952.zip", self.file_list)


#
class TestUnzip(unittest.TestCase):

    def setUp(self):
        for file in get_files(directory):
            unzip(file, directory)
        self.unzipped_file_list = get_files(os.path.join(directory, "unzipped"))

    def test_unzip_works_correct(self):
        # ToDo : reformat the assertions
        self.assertIn("w00633066A22.txt", self.unzipped_file_list)
        self.assertIn("w006330661M2.txt", self.unzipped_file_list)
        self.assertIn("w00633066952.txt", self.unzipped_file_list)
