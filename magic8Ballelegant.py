import random

messages = ['It is certain',
            'It is decidely so',
            'I can\'t imagine it to be',
            'Yes',
            'Never in a million years',
            'concentrate and ask again',
            'it\'s a bit hazy, try again',
            'Very doubtful',
            'Maybe']

print(messages[random.randint(0, len(messages) - 1)])
