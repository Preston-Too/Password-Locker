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

    def login(self):
        """
        method that allows a user to log in after providing credentials
        """
        print(" Successfully Logged in")

    def saveUser(self):
        """
        method that save user to the list
        """
        User.userList.append(self)

    @classmethod
    def displayUser(cls):
        """
        method that displays saved users
        """
        return cls.userList