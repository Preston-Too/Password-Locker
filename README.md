# Password-Locker
## Author
[Preston-Too](https://github.com/Preston-Too)

## Description
Password Locker is a python project that enables the user to save their account details and passwords. The application saves the users details and generating new passwords.

## User Stories
What the user does...
* Create an account for the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Password locker generates a new password for a user that does not have a registered account
* Password locker enables the user to delete accoun credentials that they no longer require.

## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Preston-Too/Password-Locker.git```

* cd Password

* code . to open in visual studio code.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ python3 user.py
* To run test for the application
        $ python3 user_test.py


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./user.py```|Hello Welcome to your Password Locker... <br>* cc ---  Create New Account * lg ---  Login |
|Select  cc| input username and password.cc----to type your own password,sgp----system generated password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select lg  | Enter your password and username you signed up with|  Choices to help you navigate through the application|
|Save new credential in the application| Enter ```nc```|Enter Account's name, Accounts' username, Account's password<br>choose ```cp``` to enter your password or ```sgp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```ds```|A list of all credentials that has been stored or ```You don't have any credentials saved``` |
|Search a stored credential based on account name|Enter ```fc```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want |Enter ```dc```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exist|
|Exit the application| Enter ```ex```| The application says bye and exits|

## Technologies Used

* python3.8

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [toopreston@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2020 **Preston Too**