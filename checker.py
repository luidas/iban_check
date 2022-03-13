"""Code needed to run the algorithm plus a method to convert user input"""
import sys
import algorithm


def convert_user_input(user_input: str):
    """
    Removes indents and spaces.
    Splits on newlines.
    Splits on commas.
    Flattens the list.
    Removes duplicates.
    """
    no_whitespace = user_input.replace(" ", "").replace("\t", "")
    input_lines = no_whitespace.splitlines()
    comma_split = [line.split(",") for line in input_lines]
    ibans = [iban for sublist in comma_split for iban in sublist]
    ibans_unique = list(set(ibans))
    return ibans_unique


def check_input_file(file_path):
    """
    Reads input file
    Converts user input
    Uses algorithm to check all comma or newline separated values
    """
    with open(file_path, mode="r", encoding="utf8") as file:
        user_input = file.read()
        file.close()
    ibans = convert_user_input(user_input)
    checked_ibans = [
        (iban, "valid" if algorithm.check_iban(iban) else "invalid")
        for iban in ibans
    ]
    return checked_ibans


if __name__ == "__main__":
    path = sys.argv[1]
    for iban in check_input_file(path):
        print(iban[0] + ": " + iban[1])
