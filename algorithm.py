"""
Module to check iban. Does not validate bban.
Provides some helper functions and a registry.
"""
import json
import string

from pathlib import Path


with open(Path("iban_registry.json"), encoding="utf8") as f:
    REGISTRY = json.load(f)


LETTERS = {
    letter: (10 + index) for index, letter in enumerate(string.ascii_uppercase)
}


def check_length(iban: str) -> bool:
    """Return True if IBAN length is correct per the country."""
    country_code = iban[0:2]
    if country_code in REGISTRY.keys():
        return REGISTRY[country_code]["iban_length"] == len(iban)
    return False


def rearrange(iban: str) -> str:
    """Return the IBAN with first 4 characters at the end"""
    return iban[4:] + iban[:4]


def convert_to_integer(iban: str) -> int:
    """
    Return IBAN with each letter replaced with two digits,
    where A = 10, B = 11, ..., Z = 35
    """
    integer = ""
    for char in iban:
        if char.isalpha():
            integer += str(LETTERS[char.upper()])
        else:
            integer += char
    return int(integer)


def validate_iban(iban: str) -> bool:
    """
    If length is valid:
    1. Rearrange
    2. Convert to integer
    3. Return if mod 97 remainder is equal to 1
    """
    return check_length(iban) and convert_to_integer(rearrange(iban)) % 97 == 1


def replace_check_digits(iban: str) -> str:
    """Returns iban with 00 as country code"""
    return iban[0:2] + "00" + iban[4:]


def calculate_check_digits(iban: str) -> int:
    """
    1. Make country code 00
    2. Move first 4 characters to the end
    3. Return the difference between 98 and the remainder of mod 97
    """
    return 98 - (
        convert_to_integer(rearrange(replace_check_digits(iban))) % 97
    )


def check_iban(iban: str) -> bool:
    """
    1. Check if iban is string
    2. Remove all spaces
    3. Check if characters at check digit position are digits
    4. Calculate check digits
    5. Return True if iban is valid and calculated check digits = check digits
    """
    if not isinstance(iban, str):
        return False
    iban = iban.replace(" ", "")  # Parse
    check_digits = iban[2:4]
    if not check_digits.isdigit():
        return False
    return validate_iban(iban) and calculate_check_digits(iban) == int(
        check_digits
    )
