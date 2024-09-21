#!/usr/bin/env python3
""" This is the Database Module """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session
import bcrypt

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> Session:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adding a user to the database """
        new_user = User(email=email, hashed_password=hashed_password)

        self._session.add(new_user)

        self._session.commit()

        self._session.refresh(new_user)

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Finds a user by arguments"""

        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No User Found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid Request")

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Updates a user"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError("User does not have attribute")
            setattr(user, key, value)

        self._session.commit()

    def _hash_password(self, password: str) -> bytes:
        """ Hashes a password """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
