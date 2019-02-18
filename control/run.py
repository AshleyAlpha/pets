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
