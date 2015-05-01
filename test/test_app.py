import unittest
from app.main import get_files


class TestGetFiles(unittest.TestCase):

    def setUp(self):
        directory = "test/test_data/test_statements"
        self.file_list = get_files(directory)

    def test_get_files_returns_correct_list(self):
        self.assertIn("w00633066A22.zip", self.file_list)
        self.assertIn("w006330661M2.zip", self.file_list)
        self.assertIn("w00633066952.zip", self.file_list)
