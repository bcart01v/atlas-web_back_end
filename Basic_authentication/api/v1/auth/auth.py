#!/usr/bin/env python3
"""
Module for managing API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns False for now, to be implemented later"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method that returns None, will handle the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that returns None, will retrieve the current user"""
        return None
