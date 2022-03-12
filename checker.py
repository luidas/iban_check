import sys
import algorithm


def convert_user_input(input: str):
    no_spaces = input.replace(" ", "")
    input_lines = no_spaces.splitlines()
    comma_split = [line.split(",") for line in input_lines]
    ibans = [iban for sublist in comma_split for iban in sublist]
    return ibans


def check_input_file(path):
    file = open(path, "r")
    input = file.read()
    ibans = convert_user_input(input)
    checked_ibans = [
        (iban, "valid" if algorithm.check_iban(iban) else "invalid")
        for iban in ibans
    ]
    return checked_ibans


if __name__ == "__main__":
    path = sys.argv[1]
    checked_ibans = check_input_file(path)
    for iban in checked_ibans:
        print(iban[0], iban[1])
