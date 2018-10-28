import pytest
from user import User

user1 = User("Aaron", "madCat243", "IT", 283929, 2135239929)

def get_username(user):
    return user.username

def get_password(user):
    return user.password

def get_role(user):
    return user.role

def get_id(user):
    return user.id

def get_phone(user):
    return user.phone

def test_username():
    assert get_username(user1) == "Aaron"

def test_password():
    assert get_password(user1) == "madCat243"

def test_role():
    assert get_role(user1) == "IT"

def test_id():
    assert get_id(user1) == 283929

def test_phone():
    assert get_phone(user1) == 2135239929
