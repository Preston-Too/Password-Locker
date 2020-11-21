import random
import string
import pyperclip

class User:
    """
    Creates a user class that generates new intances of the User.
    """

    userList = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLoggedin = False

    def createUser(username, password):
        """
        method to create new user account
        """
        newUser = User(username, password)
        return newUser