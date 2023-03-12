import unittest
from unittest.mock import patch
import os
import tempfile
import shutil
from p_terraformer.utils.helpers import generate_filename, file_handling, terraform_init
from p_terraformer.cmd.terraform_generator import generation_datadog

class test_generate_filename(unittest.TestCase):

    def test_add_datadog_profile(self):
        output = generate_filename()
        self.assertRegex(output, r"\d{4}-\d{2}-\d{2}-\d{2}-\d{2}")

class test_terraform_init(unittest.TestCase):

    def test_terraform_init(self):
        generation_datadog("0.13.6", "3.12.0")
        terraform_init()

if __name__ == '__main__':
    unittest.main()