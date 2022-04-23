import random
import string
import unittest #importing unittest module
from credentials import Credentials #importing credentials class

class TestCredentials(unittest.TestCase):
    '''
    test class that defines test cases for the credentials behaviours
    
    Args: 
        unittest.TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        setUp method to run before each test case
        '''
        
        self.new_credential = Credentials("twitter","ckimani882","catherine")
        
    def test_init(self):
        '''
        test init case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"ckimani882")
        self.assertEqual(self.new_credential.pass_word,"catherine")
        
        Credentials.credentials_list = []
        
    def test_save_credential(self):
        '''
        test_save_credential to test if the credential object is saved into the credentials_list
        '''
        
        self.new_credential.save_credential() #saving nwe credential
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from the credential_list
        '''
        
        self.new_credential.save_credential()
        test_credential = Credentials("twitter","kaykate899","ckay")
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_user_by_account(self):
        '''
        test to check if we can find a credential by account name and display information
        '''
        
        self.new_credential.save_credential()
        test_credential = Credentials("twitter", "caroline", "carol123") #new credential
        test_credential.save_credential()
        
        found_credential = Credentials.find_user_by_account("twitter")
        self.assertEqual(found_credential.account, test_credential.account)
        
    def test_find_credential_exist(self):
        '''
        test to check if we can return a boolean if a credential is not found
        '''
        
        self.new_credential.save_credential()
        test_credential = Credentials("twitter","ckimani882","catherine")
        test_credential.save_credential()
        
        credential_exist = Credentials.find_credential_exist("twitter")
        self.assertTrue(credential_exist)
        
    def test_display_credentials_list(self):
        '''
        method that returns a list of all credentials
        '''
        
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
if __name__ == '__main__':
    unittest.main()