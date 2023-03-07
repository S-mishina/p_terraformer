import unittest
import os
import tempfile
from p_terraformer.config.cli_conf import profile_check

class TestGenerationAWS(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)
        os.environ["HOME"] = self.tmpdir.name
        self.temp_file_path = os.path.join(self.tmpdir.name, ".p_terraformer", "config.yaml")
        os.makedirs(os.path.dirname(self.temp_file_path), exist_ok=True)
        with open(self.temp_file_path, "w") as f:
            f.write("")

    def test_add_datadog_profile(self):
        profile_check()

if __name__ == '__main__':
    unittest.main()