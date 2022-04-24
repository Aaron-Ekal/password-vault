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

def save_user(user):
    '''
    Function takes in the user returned above and saves it using the save_user method from the User class
    '''
    User.save_user(user)

def check_user(user_name, password):
    '''
    Function to see if the user exists in user_list
    '''
    check_user = Credentials.confirm_user(user_name, password)
    return check_user

def new_credentials(website_name, user_name, password):
    '''
    Function using the Credentials class to build a new_credentials
    Args:
    site_name: Website to which the credentials belong to
    user_name: The websites user_name
    password: The website's password
    Returns: new_credentials
    '''
    new_credentials = Credentials(website_name, user_name, password)
    return new_credentials

def save_credentials(credentials):
    '''
    function taking in the credentials and saving them to the credentials_list
    '''
    Credentials.save_credentials(credentials)

def list_credentials(user):
    '''
    Function calling the list_credentials method in Credntials to list credentials per user
    '''
    return Credentials.list_credentials(user)

def password_builder():
    '''
    function calling the password builder from Credentials class
    '''
    password = Credentials.password_builder()
    return password
