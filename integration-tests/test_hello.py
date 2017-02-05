import requests
import time
import unittest


class ViewsTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        time.sleep(5)

    def testhello(self):
        r = requests.get("web:8000")
        self.assertIn("hello", r)

if __name__ == '__main__':
    unittest.main()