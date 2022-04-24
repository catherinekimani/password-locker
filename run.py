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
    new_credentials = Credentials(account,username,pass_word)
    return new_credentials

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
    print("\n")
    
    while True:
        print("Use these short codes to navigate through: \n 1. New User - NU, \n 2. Login to your account - LG,  \n 3. Display credentials - DC, \n 4. Create Credential - CC  \n 5. Exit - EX" )
        
        short_code = input().upper()
        if short_code == 'NU':
            print("New User")
            print("-" * 10)
            
            print("Enter fullname")
            fullname= input()
            
            print("Enter Password...")
            password = input()
            print("Confirm Password")
            password = input()
            
            save_user(create_user(fullname,password)) #create and save new user account
            
            print('\n')
            print(f"Congratulations!! {fullname} New Account Successfully Created")
            print('\n')
            print("Proceed to Login!!")
            print("Enter Short code (LG)")
            
        elif short_code == 'LG':
            print("Login to your account!!")
            print("Welcome....")
            print("Enter Username")
            username = input()
            
            print("Enter Password")
            password = input()
            print(f" Hello {username} Welcome to password Locker!")
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
                print("\n")
                print("Create a new Credential")
                print("\n")
                
            if short_code == 'EX':
                print("Exit Password Locker .........")
                print("Please Wait")
                break
            else:
                print("Invalid Short_code")
                print("Please input the correct short code to continue")
if __name__ == '__main__':
    main()