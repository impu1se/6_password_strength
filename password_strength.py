import argparse
import re
from string import punctuation
from getpass import getpass


def get_black_list(file_list):
    with open(file_list, 'r') as file:
        black_list = file.read().split()
        return black_list


def get_user_password():
    return getpass('Input your password without space: ')


def get_password_strength(password, black_list):
    score = 0
    safe_length = 8
    patterns = [r'[a-z]', r'[A-Z]', r'[0-9]', r'[{}]'.format(punctuation)]
    for pattern in patterns:
        if re.search(pattern, password):
            score += 1
    if len(password) >= safe_length:
        score += 3
    if len(password) == len(set(password)) and len(password) >= safe_length:
        score += 3
    if password in black_list and password != '':
        score = 2
    return score


def main():
    parser = argparse.ArgumentParser(
        description='Show to how much your password is reliable')
    parser.add_argument(
        '-f', 
        dest='file', 
        help='Indicate file for black list'
        )
    args = parser.parse_args()
    password = get_user_password()
    if ' ' not in password and 'txt' in args.file:
        black_list = get_black_list(args.file)
        score = get_password_strength(password, black_list)
        print('Your score is: {}'.format(score))
    else:
        print("""You didn't input password or file with black list.
            For help enter the password_strength.py -h""")


if __name__ == '__main__':
    main()
