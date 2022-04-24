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


    def save_credentials(self):
        '''
        saves new instances to credentials_list array
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        removes existing instances from credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_site_name(cls, website_name):
        '''
        this method takes in website_name & returns the credentials tat match the website_name
        Args:
            website_name: site name to search for
        Returns:
            login credentials of the website
        '''
        for credential in cls.credentials_list:
            if credential.website_name == website_name:
                return credential