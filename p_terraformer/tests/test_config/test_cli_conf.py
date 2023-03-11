import unittest
import os
import tempfile
from p_terraformer.config.cli_conf import profile_check

class TestGenerationAWS(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)
        os.environ["HOME"] = self.tmpdir.name

    def test_add_datadog_profile(self):
        output=profile_check()
        self.assertEqual(output["profile"], [])

if __name__ == '__main__':
    unittest.main()