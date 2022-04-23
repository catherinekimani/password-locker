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
        
    def test_find_user_by_account(self):
        '''
        test to check if we can find a credential by account name and display information
        '''
        
        self.new_credential.save_credential()
        test_credential = Credentials("twitter", "caroline", "carol123") #new credential
        test_credential.save_credential()
        
        found_credential = Credentials.find_user_by_account("twitter")
        self.assertEqual(found_credential.account, test_credential.account)
        
if __name__ == '__main__':
    unittest.main()