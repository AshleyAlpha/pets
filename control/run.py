from user import User
from credentials import Credentials
def create_user(email,username,password):
    '''
    Function to create a new user
    '''
    new_user = Users(email,username,password)
    return new_user

    def create_credential(app_name,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(app_name,password)
    return new_credential
def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()

def save_credential(credential):
    '''
    Function to save new credential
    '''
    credential.save_credential()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return user.find_by_username(username)

def find_credential(app_name):
    '''
    Function that finds a credential by app_name and returns the credential
    '''
    return Credentials.find_by_app_name(app_name)

def check_existing_user(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return Users.user_exist(username)
    def check_existing_credential(app_name):
    '''
    Function that check if a credential exists with that app_name and return a Boolean
    '''
    return Credentials.credential_exist(app_name)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return Users.display_user()

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credential()

def main():
    print("Hello Welcome to your users list. What is your name?")
    user_name = input()