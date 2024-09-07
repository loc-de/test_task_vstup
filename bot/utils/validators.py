import re


def is_valid_amount(amount):
    pattern = r'^-?\d+(\.\d+)?$'
    return re.match(pattern, amount) is not None
