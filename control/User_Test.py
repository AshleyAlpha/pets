import unittest # Importing the unittest module
from users import Users # Importing the contact class

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the Users class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
         #setup method to run before each test cases.
        
        self.new_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.email,"mashleyalpha@gmail.com")
        self.assertEqual(self.new_user.username,"ashleyalpha")
        self.assertEqual(self.new_user.password,"miahmamie")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the users list
        '''
        self.new_user.save_user() # saving the new users
        self.assertEqual(len(Users.users_list),1)
    
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our users_list
            '''
            self.new_user.save_user()
            test_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # new user
            test_user.save_user()
            self.assertEqual(len(Users.users_list),2)
#setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Users.users_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our users_list
            '''
            self.new_user.save_user()
            test_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # new user
            test_user.save_user()
            self.assertEqual(len(Users.users_list)
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # new user
        test_user.save_user()

        found_user = Users.find_by_username("ashleyalpha")

        self.assertEqual(found_user.email,test_user.email)
    
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = Users("uwinezaandersonne@gmail.com","UwinezaAdolatha","Andy") # new user
        test_user.save_user()

        user_exists = Users.user_exist("uwinezaandersonne@gmail.com")

        self.assertTrue(user_exists)