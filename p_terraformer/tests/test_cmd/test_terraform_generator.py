import unittest
import os

from p_terraformer.cmd.terraform_generator import generation_aws
from p_terraformer.cmd.terraform_generator import generation_datadog

class test_generation_aws(unittest.TestCase):

    def test_generation_aws(self):
        generation_aws("0.13.6", "3.12.0", "ap-northeast-1")
        self.assertTrue(os.path.isfile("main.tf"))
        os.remove("main.tf")

class test_generation_datadog(unittest.TestCase):

    def test_generation_datadog(self):
        generation_datadog("0.13.6", "3.12.0")
        self.assertTrue(os.path.isfile("main.tf"))
        os.remove("main.tf")

if __name__ == '__main__':
    unittest.main()
