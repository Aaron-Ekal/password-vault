import random, string
from user_login import User


class Credentials:
    '''
    Credentials class to create new credentials instances
    '''

    credentials_list = []

    def __init__(self, website_name, user_name, password):
        '''
        __init__ to define properties of new Credentials
        Args:
            website_name: Website in which the credentials belong to.
            user_name: username for websites account
            password: password for the account
        '''

        self.website_name = website_name
        self.user_name = user_name
        self.password = password 