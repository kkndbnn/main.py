import unittest
from tests.file import do_disk


class TestFunctions(unittest.TestCase):
    def test_do_disk(self):
        req = do_disk()
        self.assertEqual(str(req), '<Response [200]>')