# database.py
from werkzeug.security import generate_password_hash
authusers = {
   #usernames for testing
    'mihir2780': {
        'name': 'mihir',
        'password': generate_password_hash('password1'),
        'date_of_birth': '1998-10-02',
        'address': 'India'
    },
    'ejay2780': {
        'name': 'ejay',
        'password': generate_password_hash('password2'),
        'date_of_birth': '1995-05-15',
        'address': 'United Kingdom'
    },
    'chris2780': {
        'name': 'chris',
        'password': generate_password_hash('password3'),
        'date_of_birth': '1993-03-15',
        'address': 'United Kingdom'
    }
}

