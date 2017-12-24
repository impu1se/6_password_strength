import argparse
import re
from getpass import getpass


def get_black_list(file_list):
    with open(file_list, 'r') as f:
        black_list = f.read().split()
        return black_list


def get_user_password():
    return getpass('Input your password: ')


def get_password_strength(password, black_list):
    score = 0
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[$#@]', password):
        score += 2
    if re.search(r'\s', password):
        score += 1
    if len(password) >= 8:
        score += 2
    # if len(password) > len(set(password)) * 0.7:
    #     score += 2
    if password in black_list:
        score = 2
    print('Your score is:', score)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show how much your password is reliable')
    parser.add_argument('-f', dest='file',
                        help='Indicate file for black list')
    args = parser.parse_args()
    password = get_user_password()
    black_list = get_black_list(args.file)
    get_password_strength(password, black_list)