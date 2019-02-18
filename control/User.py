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