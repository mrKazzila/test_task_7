import re

__DATA_REGEX_PATTERN = re.compile(r'^(\d{2}\.\d{2}.\d{4}|\d{4}-\d{2}-\d{2})$')
__PHONE_REGEX_PATTERN = re.compile(r'^\+\d \d{3} \d{3} \d{2} \d{2}$')
__EMAIL_REGEX_PATTERN = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)


def validate_date(date: str) -> bool:
    return bool(__DATA_REGEX_PATTERN.match(date))


def validate_phone(phone: str) -> bool:
    return bool(__PHONE_REGEX_PATTERN.match(phone))


def validate_email(email: str) -> bool:
    return bool(__EMAIL_REGEX_PATTERN.match(email))
