#!/usr/bin/env python3
""" BasicAuth module for API authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts base64 part of the authorization header for baisc auth"""

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[len('Baisc '):]

    def decode_base64_authorization_header(
            self, base64_authorization_header:str) -> str:
        """ Decodes base64 part of the authorization header for basic auth"""

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decode_base = base64.b64decode(base64_authorization_header)
            return decode_base.decode('utf-8')
        except Exception:
            return None
