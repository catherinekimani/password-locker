class User:
    '''
    class that generates new instances of users
    '''
    
    user_list = [] #empty user list
    
    def __init__(self,user_name,password):
        '''
        init method to define properties of our objects
        Args:
            user_name: new user username
            password: new user password
        '''
        
        self.user_name = user_name
        self.password = password