#!/usr/bin/env python3
"""Filtering data from log messages"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated """
    pattern = '|'.join([f'{field}=[^ {separator}]+' for field in fields])
    return re.sub(
        pattern,
        lambda x: f"{x.group().split('=')[0]}={redaction}",
        message
    )
