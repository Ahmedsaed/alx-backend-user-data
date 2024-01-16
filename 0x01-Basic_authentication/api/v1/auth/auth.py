#!/usr/bin/env python3
"""
Route module for the API Authentification
"""

from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    """
    Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            - path(str): Url path to be checked
        Return:
            - False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance from information from a request object
        """
        return None
