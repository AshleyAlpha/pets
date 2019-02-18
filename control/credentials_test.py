import unittest # Importing the unittest module
from credentials import Credentials # Importing the contact class
class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("facebook","miahmamie") # create credential object
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.app_name,"facebook")
        self.assertEqual(self.new_credential.password,"miahmamie")
def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credentials list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1) 
