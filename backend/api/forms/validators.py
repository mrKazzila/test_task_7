import re

DATA_REGEX_PATTERN = re.compile(r'^(\d{2}\.\d{2}.\d{4}|\d{4}-\d{2}-\d{2})$')
PHONE_REGEX_PATTERN = re.compile(r'^\+\d{1,3} \d{1,4} \d{1,4} \d{1,2} \d{1,2}$')
EMAIL_REGEX_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


def validate_date(date: str) -> bool:
    return bool(DATA_REGEX_PATTERN.match(date))


def validate_phone(phone: str) -> bool:
    return bool(PHONE_REGEX_PATTERN.match(phone))


def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX_PATTERN.match(email))
