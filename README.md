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
|Open the application on the terminal | Run the command ```$ ./python3 user.py```|Hello Welcome to your Password Locker...
* cc --- Create New Account * lg --- Login <br>*
|Select cc| input username and password.cc----to type your own password,sgp----system generated password| Your account has been created successfully.`|
|Select lg | Enter your password and username you signed up with| There are choices to help the user in moving from one step to the other|
|Save new credential in the application  | Enter sc|Enter account,username,password & Choose to enter own password or system generated password|
|Display all stored credentials |  Enter ds| A list of all credentials that has been stored or You don't have any credentials saved yet|
|Finf stored credential based on account name  |  Enter fc| Enter the Account you want to search for and returns the account details|
|Delete credential| Enter dc | Enter the account of the Credentials you want to delete |
| Exit the application | Enter ex | The application bids you bye and exits |

## Technologies Used

* python3.8

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [toopreston@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2020 **Preston Too**