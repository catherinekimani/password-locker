from os import access
from user import User
from credentials import Credentials
import random

def create_user(fullname,password):
    '''
    function  to create a new user
    '''
    
    new_user = User(fullname,password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
    
def delete_user(user):
        '''
        function to delete user
        '''
        user.delete_user()
        
def find_user(username):
    '''
    function that finds user by name and returns the user
    '''
    return User.find_by_user(username)

def user_exists(username):
    '''
    function that checks if user exists and returns a boolean
    '''
    return User.user_exists(username)

#credentials 
def create_Credentials(account,username,pass_word):
    '''
    function to create new credentials
    '''
    credentials = Credentials(account,username,pass_word)
    return credentials

def save_credentials(credentials):
    '''
    function to save a credential
    '''
    credentials.save_credentials()
    
def delete_credential(credentials):
    '''
    function to delete credential
    '''
    credentials.delete_credentials()
    
def credential_exist(account):
    '''
    function that checks if  a credential exists by account and returns a boolean
    '''
    return Credentials.find_credential_exist(account)

def display_credentials():
    '''
    function that returns all saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Welcome to Password Locker")
    print("*" * 80)
    print("\n")
    
    while True:
        print("Use these short codes to navigate through: \n 1. New User - NU, \n 2. Login to your account - LG,  \n 3. Display credentials - DC, \n 4. Create Credential - CC \n 5. Generate password - GP \n 6. View Account - VA  \n 7. Exit - EX" )
        print("\n")
        
        short_code = input().upper()
        if short_code == 'NU':
            print("New User")
            print("*" * 80)
            
            print("Enter fullname")
            fullname= input()
            
            print("Enter Password...")
            password = input()
            print("Confirm Password")
            password = input()
            
            save_user(create_user(fullname,password)) #create and save new user account
            
            print('\n')
            print(f"Congratulations!! {fullname} New Account Successfully Created")
            print("*" * 80)
            print('\n')
            print("Proceed to Login!!")
            print("*" * 80)
            print("Enter Short code (LG)")
            print("*" * 80)
            
        elif short_code == 'LG':
            print("Login to your account!!")
            print("*" * 80)
            print("Welcome....")
            print("*" * 80)
            print("Enter Username")
            username = input()
            
            print("Enter Password")
            password = input()
            print(f" Hello {username} Welcome to password Locker!")
            print("*" * 80)
            print("\n")
            
        elif short_code == 'DC':
            
            if display_credentials():
                print("Here are your credentials")
                print("\n")
                
                for Credentials in display_credentials():
                    print(f"{Credentials.account} \n {Credentials.password} \n {Credentials.username}")
                    print("\n")
            else:
                print("\n")
                print("Ooops You don't seem to have any saved Credentials yet ")
                print("*" * 80)
                print("\n")
                print("Create a new Credential")
                print("*" * 80)
                print("\n")
                
        elif short_code == 'CC':
                    print("Account Name \n 1. Twitter \n 2. Facebook \n 3. Instagram")
                    print("*" * 80)
                    print("Enter Account Username")
                    username = input()
                    print("*" * 80)
                    print("Enter Password")
                    password = input()
                    print("*" * 80)
                    print("\n")
                    print("Your Account has been successfully Created")
                    print("*" * 80)
                    print("/n")
                    
        elif short_code == 'GP':
                    print("Would you like a generated password??")
                    print("*" * 80)
                    
        elif short_code == 'EX':
                print("*" * 80)
                print("Exit Password Locker .........")
                print("*" * 80)
                print("Please Wait")
                print("\n")
                print("*" * 80)
                print("Logged out")
                break
        else:
            print("Invalid Short_code")
            print("Please input the correct short code to continue")
if __name__ == '__main__':
    main()
    