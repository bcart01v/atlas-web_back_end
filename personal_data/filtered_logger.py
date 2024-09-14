#!/usr/bin/env python3
"""Filtering data from log messages"""
import re


def filter_datum(fields, redaction, message, separator):
    """Replace sensitive data with redaction in message"""
    pattern = '|'.join([f'{field}=[^ {separator}]+' for field in fields])
    return re.sub(pattern,
                  lambda x: f"{x.group().split('=')[0]}={redaction}", message)
