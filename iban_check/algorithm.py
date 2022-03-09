"""
Module to check iban. Does not validate bban.
Provides some helper functions and a registry.
"""
import json
import string
import os

file_directory = os.path.dirname(__file__)

with open(file_directory + "/iban_registry.json", encoding="utf8") as f:
    REGISTRY = json.load(f)


LETTERS = {
    letter: (10 + index) for index, letter in enumerate(string.ascii_uppercase)
}


def check_length(iban: str) -> bool:
    """Return True if IBAN length is correct per the country."""
    country_code = iban[0:2]
    if country_code in REGISTRY.keys():
        return REGISTRY[country_code]["iban_length"] == len(iban)
    else:
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
    return check_length(iban) and convert_to_integer(rearrange(iban)) % 97 == 1


def replace_check_digits(iban: str) -> str:
    return iban[0:2] + "00" + iban[4:]


def calculate_check_digits(iban: str) -> int:
    return 98 - (
        convert_to_integer(rearrange(replace_check_digits(iban))) % 97
    )


def check_iban(iban: str) -> bool:
    if type(iban) is not str:
        return False
    iban = iban.replace(" ", "")  # Parse
    check_digits = iban[2:4]
    if not check_digits.isdigit():
        return False
    return validate_iban(iban) and calculate_check_digits(iban) == int(
        check_digits
    )
