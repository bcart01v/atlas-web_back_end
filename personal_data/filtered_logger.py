#!/usr/bin/env python3
"""Filtering data from log messages"""
import re
import logging
import os
import mysql.connector
from mysql.connector import connection
from typing import List


def get_db() -> connection.MySQLConnection:
    """Establishes a connection to the MySQL database using
    credentials from environment variables"""

    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    conn = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return conn


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated """
    pattern = '|'.join([f'{field}=[^ {separator}]+' for field in fields])
    return re.sub(
        pattern,
        lambda x: f"{x.group().split('=')[0]}={redaction}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter sensitive information from log messages"""
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Creates and returns a logger that handles PII information."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger

def main():
    """Main function to retrieve and log user data."""
    logger = get_logger()
    db_connection = get_db()
    cursor = db_connection.cursor()

    cursor.execute("SELECT name, email, phone, ssn,"
                   "password, ip, last_login, user_agent FROM users")

    rows = cursor.fetchall()

    columns = ["name", "email", "phone", "ssn", "password",
               "ip", "last_login", "user_agent"]

    for row in rows:
        user_data = "; ".join([f"{col}={val}" for col, val in zip(columns, row)]) + ";"
        logger.info(user_data)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()