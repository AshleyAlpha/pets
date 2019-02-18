class Users:
    users_list = []
    def __init__(self,email, username, password):

        
        self.email = email
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into users_list
        '''
        Users.users_list.append(self)
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.
        Args:
            username: username to search for
        Returns :
            username of person that matches the username.
        '''

        for user in cls.users_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,email):
        '''
        Method that checks if a user exists from the users list.
        Args:
            email: email to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.users_list:
            if user.email == email:
                    return True

        return False