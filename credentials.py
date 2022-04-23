class Credentials:
    '''
    class that generates new instances of user's credentials
    '''
    
    credentials_list = [] #empty credentials list
    
    def __init__(self,account,username,pass_word):
        '''
        init method to define properties of our objects
        Args:
                account = new account
                username = new username
                pass_word = new password
        '''
        
        self.account = account
        self.username = username
        self.pass_word = pass_word