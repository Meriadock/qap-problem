import hello    # The code to test
import unittest   # The test framework

class Test_TestIncrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(hello.increment(3), 4)

if __name__ == '__main__':
    unittest.main()