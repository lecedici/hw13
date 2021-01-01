import unittest
import check_4errors

class MyTestCase(unittest.TestCase):
    def test_find_error(self):
        self.assertTrue(check_4errors.find_error())


if __name__ == '__main__':
    unittest.main()