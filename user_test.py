import unittest #importing the unittest module
from user import User #importing user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test case
        '''
        
        self.new_user = User("catherine kimani","123456") #create user object
        
    def test_init(self):
        '''
        test init case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_user.user_name,"catherine kimani")
        self.assertEqual(self.new_user.password,"123456")
        
    def test_save_user(self):
        '''
        test_user_save test caseto test if the user object is saved into  the user_list
        '''
        
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()