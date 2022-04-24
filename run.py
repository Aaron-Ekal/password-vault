#!/usr/bin/env python3.8

from secrets import choice
from user_login import User
from credentials import Credentials

def new_user(first_name, sur_name, user_name, email, password):
    '''
    Function using the User class to build a new_user
    Args:
    first_name: user's first name
    sur_name: user's surname
    user_name: user name to login
    email: email to login
    password: user's new password
    Returns: new_user
    '''
    new_user = User(first_name, sur_name, user_name, email, password)
    return new_user