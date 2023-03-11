import os
import tempfile
import unittest
from unittest import mock
from p_terraformer.config.cli_conf import profile_check
from p_terraformer.cmd.p_terraformer_config_generator import add_datadog_profile

class test_add_datadog_profile(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)
        os.environ["HOME"] = self.tmpdir.name

    def test_add_datadog_profile(self):
        profile_name = "test_profile"
        api_key = "test_api_key"
        app_key = "test_app_key"
        with mock.patch('builtins.input', side_effect=[profile_name, api_key, app_key]):
            command_output=add_datadog_profile()
            data=profile_check()
            result = [d for d in data["profile"] if d['name'] == profile_name]
            self.assertEqual(command_output, None)
            self.assertEqual(result[0]["api_key"], "test_api_key")
            self.assertEqual(result[0]["app_key"], "test_app_key")

    def test_add_datadog_profile1(self):
        profile_name = "test_profile"
        api_key = ""
        app_key = "test_app_key"

        with mock.patch('builtins.input', side_effect=[profile_name, api_key, app_key]):
            command_output=add_datadog_profile()
            self.assertEqual(command_output, "profile_name or api_key or app_key None")


    def test_add_datadog_profile2(self):
        profile_name = "test_profile"
        api_key = "test_api_key"
        app_key = ""

        with mock.patch('builtins.input', side_effect=[profile_name, api_key, app_key]):
            command_output=add_datadog_profile()
            self.assertEqual(command_output, "profile_name or api_key or app_key None")

    def test_add_datadog_profile3(self):
        profile_name = ""
        api_key = "test_api_key"
        app_key = "test_app_key"

        with mock.patch('builtins.input', side_effect=[profile_name, api_key, app_key]):
            command_output=add_datadog_profile()
            self.assertEqual(command_output, "profile_name or api_key or app_key None")

    def test_add_datadog_profile5(self):
        profile_name = ""
        api_key = ""
        app_key = ""

        with mock.patch('builtins.input', side_effect=[profile_name, api_key, app_key]):
            command_output=add_datadog_profile()
            self.assertEqual(command_output, "profile_name or api_key or app_key None")
if __name__ == '__main__':
    unittest.main()