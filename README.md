# iban_check

iban_check is a Python program made to check [IBAN's](https://en.wikipedia.org/wiki/International_Bank_Account_Number). For example, input like this:
```console
$ cat ibans_input.txt 
	GB29NWBK60161331926819
NL91ABNA0417164300	GB29NWBK60161331926819, BE68 5390 0754 7034
GB29 NWBK 6016 1331 9268 19, dsfgfdsg
XX89 3704 0044 0532 0130 00
```
Yields this output:
```console
$ python checker.py ibans_input.txt
NL91ABNA0417164300GB29NWBK60161331926819: invalid
BE68539007547034: valid
dsfgfdsg: invalid
GB29NWBK60161331926819: valid
XX89370400440532013000: invalid
```

The checker can be started through the command line or through a user interface made with Flask.

## Installation procedure
### User interface
No need to install anything. Just visit [https://iban-check.herokuapp.com/](https://iban-check.herokuapp.com/).
### Command line checker/development server
1. Install Python
2. Install pip
3. Run `pip: -r requirements.txt`

## Usage
When entering a list, separate IBANs by comma/newline.
### User interface
1. Open [https://iban-check.herokuapp.com/](https://iban-check.herokuapp.com/) or run the development server with `python app.py`.
2. Enter the IBAN list to the text area.
3. Press validate.
### Command line
1. Enter the IBAN list to a file (such as txt or csv).
2. Run `python checker.py example_path.txt`.


## Information on modules and functions
To open the documentation generated from docstrings open [the index page](html/iban_check/index.html) in your browser. For example run: `firefox html/iban_check/index.html`.