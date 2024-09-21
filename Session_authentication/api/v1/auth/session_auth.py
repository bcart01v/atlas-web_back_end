#!/usr/bin/env python3
""" SessionAuth module for api auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session ID for a given USER ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid. uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns the user ID based on the session ID
        """

        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a user based on session ID"""

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes the user session (Which means log out)"""

        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True