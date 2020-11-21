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

    def deleteUser(self):
        """
        method that delete a selected user
        """
        User.userList.remove(self)

if __name__ == "__main__":
    pass

class Credentials():
    """
    Method to create new credentials
    """
    credentials = []

    def __init__(self, account, username, password):
        """
        crede
        """
        self.account = account
        self.username = username
        self.password = password

    def saveCredential(self):
        """
        method that adds credentials to the list
        """
        Credentials.credentials.append(self)

    @classmethod
    def createCredential(self, account, username, password):
        """
        method that creates a new credential
        """
        newCredential = Credentials(
            account, username, password)
        return newCredential

    def searchCredential(account):
        """
        method that searches a new credential
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.account == account:
                    return credential
            print("No such account")

        else:
            print("Credentials not saved")

    def displayCredential():
        """
        methods to display saved credentials
        """
        if (len(Credentials.credentials) > 0):

            return Credentials.credentials

    @classmethod
    def credentialExist(self, accountName):
        """
        method that checks if credentials exists
        """

        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.accountName == accountName:
                    return True
            print("No such account")

        else:
            print("Not saved")

    