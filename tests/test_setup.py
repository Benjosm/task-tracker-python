# tests/test_setup.py
import os
import unittest
import subprocess

class TestSetupPy(unittest.TestCase):

    def test_setup_py_exists(self):
        self.assertTrue(os.path.exists('setup.py'))

    def test_setup_py_content(self):
        with open('setup.py', 'r') as f:
            setup_content = f.read()

        self.assertIn('name=', setup_content)
        self.assertIn('version=', setup_content)
        self.assertIn('description=', setup_content)
        self.assertIn('packages=', setup_content)

    def test_package_installable(self):
        try:
            subprocess.check_call(['python3', 'setup.py', 'install', '--user'])
        except subprocess.CalledProcessError as e:
            self.fail(f"Installation failed: {e}")

if __name__ == '__main__':
    unittest.main()