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
        
    def save_user(self):
        '''
        save user method saves user objects into user_list
        '''
        
        User.user_list.append(self)
        
    def delete_user(self):
        '''
        delete user method deletes a saved user from the user_list
        '''
        
        User.user_list.remove(self)
        
    @classmethod
    def find_by_user(cls, user_name):
        '''
        Method that takes in a user and returns a user that matches that username.
        Args:
            name: name to search for
        Returns :
            name of person that matches the password.
        '''
        
        for user in cls.user_list:
            if user.user_name == user_name:
                return user
    
    @classmethod
    def user_exists(cls, user_name):
        '''
        Method that checks if a user exists from the user details.
        Args:
        username: username to search if it exists
        Returns :
        Boolean: True or false depending if the user exists
        '''
        
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
        return False
    