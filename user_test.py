import unittest  # importing the unittest module
from user import User  # importing the User class
from user import Credentials  # importing the Credentials class
import pyperclip

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the Users class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    """
    def setUp(self):
        '''
        method to run each test
        '''
        self.user = User("Preston", "press123")

    def test_init(self):
        '''
        check proper user initialization
        '''
        self.assertEqual(self.user.username, "Preston")
        self.assertEqual(self.user.password, "press123")


if __name__ == "__main__":
    unittest.main()
