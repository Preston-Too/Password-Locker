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

    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("Ray", "12345678")  # new contact
        test_user.saveUser()

        self.assertEqual(len(User.userList), 2)

    def tearDown(self):
        '''
        method to clean up after each test
        '''

        User.userList = []

    
    def test_delete_user(self):
        """
        method to test delete users
        """
        self.user.saveUser()
        test_user = User("Ray", "12345678")  # new contact
        test_user.saveUser()

        self.user.deleteUser()
        self.assertEqual(len(User.userList), 1)

    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.userList)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        define the constructor
        """
        self.cred = Credentials("Twitter", "@prestonblazer", "press123")

    def test_init(self):
        """
        make sure the credential is well initialized
        """
        self.assertEqual(self.cred.account, "Twitter")
        self.assertEqual(self.cred.username, "@prestonblazer")
        self.assertEqual(self.cred.password, "press123")

    def tearDown(parameter_list):
        """
        clear up during each test
        """
        Credentials.credentials = []

    def test_save_multiples_credential(self):
        """
        test for multiple credentials
        """
        self.cred.saveCredential()
        test_cred = Credentials("Twitter", "@prestonblazer", "press123") 
        test_cred.saveCredential()

        self.assertEqual(len(Credentials.credentials), 2)

    def test_delete(self):
        """
        test to delete credentials
        
        """
        self.cred.saveCredential()
        test_cred = Credentials("Twitter", "@prestonblazer", "press123") 
        test_cred.saveCredential()

        self.cred.deleteCredential()
        self.assertEqual(len(Credentials.credentials), 2)


if __name__ == "__main__":
    unittest.main()
