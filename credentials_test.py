import unittest
from credentials import Credentials



class TestUser(unittest.TestCase):
    '''
    Test class to define test cases for the User class

    Args:
        unittest.TestCase: TestCase class creates test cases
    '''

    def setUp(self):
        '''
        Method to create test cases for the credentials class
        '''
        self.new_credentials = Credentials("Twitter", "AaronEkal", "qwerty123")

    def test__init__(self):
        '''
        test to check object instatiation
        '''
        self.assertEqual(self.new_credentials.website_name, "Twitter")
        self.assertEqual(self.new_credentials.user_name, "AaronEkal")
        self.assertEqual(self.new_credentials.password, "qwerty123")