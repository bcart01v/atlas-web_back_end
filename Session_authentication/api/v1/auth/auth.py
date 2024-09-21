#!/usr/bin/env python3
"""
Module for managing API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that checks if a given path requires authentication"""
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Method that returns None, will retrieve the Authorization """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that returns None, will retrieve the current user"""
        return None

    def session_cookie(self, request=None):
        """ Return value of cookie from the request"""
        if request is None:
            return None

        session_name = getenv('SESSION_NAME', '_my_session_id')

        return request.cookies.get(session_name)
