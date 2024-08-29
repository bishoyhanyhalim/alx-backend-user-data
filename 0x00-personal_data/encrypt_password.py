#!/usr/bin/env python3
"""
Password Encryption task
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """task for func 2"""
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """task for func"""
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
