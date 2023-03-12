import unittest
from unittest.mock import patch
import os
import tempfile
from p_terraformer.config.cli_conf import profile_check , aws_secret_get

class test_generation_aws(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)
        os.environ["HOME"] = self.tmpdir.name

    def test_add_datadog_profile(self):
        output=profile_check()
        self.assertEqual(output["profile"], [])

class test_aws_secret_get(unittest.TestCase):
    def setUp(self):
        os.environ["TESTING_FLAG"] = "True"
        os.environ["AWS_ACCESS_KEY_ID"] = "hogehoge"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "hogehoge"
    def test_aws_secret_get1(self):
        secret_name = "test"
        secret_value = "test"
        region_name = "ap-northeast-1"
        output = aws_secret_get(secret_name, secret_value, region_name)
        self.assertEqual(output, "test")

if __name__ == '__main__':
    unittest.main()