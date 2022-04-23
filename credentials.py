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
        
    def save_credential(self):
        '''
        save_credential method that saves credentials objects into credentials list
        '''
        
        Credentials.credentials_list.append(self)
        
    def delete_credential(self):
        '''
        delete credential method deletes a saved credential in the credentials_list
        '''
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_user_by_account(cls, account):
        '''
        Method that takes in a credential and returns a credential that matches that account.
        Args:
        account: account to search for
        Returns :
            credential of person that matches the account.
        '''
        
        for Credentials in cls.credentials_list:
            if Credentials.account == account:
                return Credentials
            
    @classmethod
    def find_credential_exist(cls,account):
        '''
        method that checks if a credential exists from the credentials list
        Args:
        account: account name to search if it exists
        Returns:
        Booleans: true or false if the credential exists
        '''
        
        for Credentials in cls.credentials_list:
            if Credentials.account == account:
                return True
            
        return False
