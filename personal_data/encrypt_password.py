#!/usr/bin/env python3
import bcrypt
""" Encrypting passwords """


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
 
    return hashed_password