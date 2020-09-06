from qap.core import hello
import unittest

class Test_TestIncrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(hello.increment(3), 4)

if __name__ == '__main__':
    unittest.main()