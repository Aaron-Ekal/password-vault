import unittest
from user_login import User


class TestUser(unittest.TestCase):
    '''
    Test class to define test cases for the User class
    Args:
        unittest.TestCase: TestCase class creates test cases 
    '''

    def setUp(self):
        '''
        Method run before each test to build a start
        '''
        self.new_user = User("Aaron", "Ekal", "Tellem", "tellem@ent.com", "123qwerty")

    def test__init__(self):
        '''
        test initialization to test object instantiation
        '''
        self.assertEqual(self.new_user.first_name, "Aaron")
        self.assertEqual(self.new_user.sur_name, "Ekal")
        self.assertEqual(self.new_user.user_name, "Tellem")
        self.assertEqual(self.new_user.email, "tellem@ent.com")
        self.assertEqual(self.new_user.password, "123qwerty")