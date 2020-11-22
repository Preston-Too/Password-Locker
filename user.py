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
    def credentialExist(self, account):
        """
        method that checks if credentials exists
        """

        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.account == account:
                    return True
            print("No such account")

        else:
            print("Not saved")

    def deleteCredential(account):
        """
        method that deletes credential
        """
        for credential in Credentials.credentials:
            if credential.username == account:
                Credentials.credentials.remove(credential)

    def passwordGenerate(stringLength=8):
        """
        method that generate a random password
        """
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))

if __name__ == "__main__":
    
    isTrue = True
    print("Welcome to password Locker.An app to manage and generate passwords.")
    while isTrue == True:
        print(
            "Use these short code to proceed:\n\n 1. cc-Create Account\n 2. lg-Login\n 3. ex-Exit")
        shortCode = input().lower()

        if shortCode == 'cc':
            print("New Account")
            print("*"*40)
            print("Username")
            username = input()

            while True:
                print(
                    "1. cp - create own password\n 2. sgp - System generated password")
                passwordOption = input()

                if passwordOption == 'cp':
                    print("Your Password")
                    password = input()
                    break
                elif passwordOption == 'sgp':
                    password = Credentials.passwordGenerate()
                    break

                else:
                    print("PasswordOption Invalid")

            createUser = User.createUser(username, password)
            User.saveUser(createUser)
            print("\n")
            print(
                f"Hi {username} You've sucessfully created you account\n")
            print(f"Your username is {username} and password is {password}\n")

        elif shortCode == 'lg':
            print("*"*60)
            print("Enter your username and password")
            print("*"*60)

            print("Username")
            username = input()
            print("Password")
            password = input()

            for user in User.userList:
                if username == user.username:
                    if user.password == password:
                        print(user.login())
                    else:
                        print("password invalid")
                        break
                else:
                    print("username Invalid")
                    break

            break

        elif shortCode == 'ex':

            print("Bye. Nice time.")
            break

        else:
            print("Invalid shortcode\n")