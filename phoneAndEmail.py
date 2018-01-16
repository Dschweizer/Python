#! /usr/bin/env python3
# PhoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # Area code
    (\s|-|\.)?              # Seperator(space between area code and number)
    (\d{3})                 # First 3 digits.
    (\s|-|\.)               # Seperator(space between first 3 digits and last 4)
    (\d{4})                 # Last 4 digits.
    (\s*(ext|x|ext.)\s*(\d{2,5})))?    #Extension
    )''', re.VERBOSE)

#TODO: Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # Username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # Domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)


#TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if group[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#TODO: Copy results to clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
